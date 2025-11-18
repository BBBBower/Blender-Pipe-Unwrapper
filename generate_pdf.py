"""
Generate exhaust wrap template PDF with exact UV unwrap outline
Shows actual shape from Blender UV unwrap
"""
import json
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, blue, red

# Load boundary data
with open("C:\\Users\\Bower\\Downloads\\boundary_data.json", 'r') as f:
    boundary = json.load(f)

with open("C:\\Users\\Bower\\Downloads\\pdf_data.json", 'r') as f:
    data = json.load(f)

boundary_edges = boundary['boundary_edges']
min_u = boundary['min_u']
max_u = boundary['max_u']
min_v = boundary['min_v']
max_v = boundary['max_v']

base_w = data['pipe_circ_mm']  # 239.4 mm
base_h = data['pipe_arc_mm']   # 35.9 mm
wrap_w = data['wrap_width']     # 283.9 mm
wrap_h = data['wrap_arc_length'] # 37.6 mm
overlap = data['overlap']        # 10 mm

# Page setup
page_w, page_h = landscape(A4)

print(f"Page size: {page_w/mm:.1f} × {page_h/mm:.1f} mm")
print(f"Base pipe: {base_w:.1f} × {base_h:.1f} mm")
print(f"Wrap layer: {wrap_w:.1f} × {wrap_h:.1f} mm")
print(f"Boundary edges: {len(boundary_edges)}")

# Create PDF
pdf_path = "C:\\Users\\Bower\\Downloads\\exhaust_wrap_template.pdf"
c = canvas.Canvas(pdf_path, pagesize=landscape(A4))

margin = 15 * mm

# Template position (centered)
template_x = (page_w - wrap_w * mm) / 2
template_y = margin + 40 * mm

# Title
c.setFont("Helvetica-Bold", 14)
c.drawCentredString(page_w/2, page_h - 15*mm, "EXHAUST WRAP CUTTING TEMPLATE")

c.setFont("Helvetica", 10)
c.drawCentredString(page_w/2, page_h - 25*mm, "3\" OD | 1.5D | Degrees per segment:")

c.setFont("Helvetica-Bold", 9)
c.setFillColor(HexColor("#CC0000"))
c.drawCentredString(page_w/2, page_h - 35*mm, "PRINT AT 100% SCALE - VERIFY SCALE BAR = 100mm")
c.setFillColor(black)

# Calculate offsets
base_offset_x = (wrap_w - base_w) / 2
base_offset_y = (wrap_h - base_h) / 2

# Draw BASE PIPE outline (blue)
print("Drawing base pipe outline...")
c.setStrokeColor(blue)
c.setLineWidth(1.0)

for edge in boundary_edges:
    v1, v2 = edge
    u1, v1_coord = v1
    u2, v2_coord = v2

    # Normalize and map to base pipe dimensions
    u1_norm = (u1 - min_u) / (max_u - min_u) if (max_u - min_u) > 0 else 0
    v1_norm = (v1_coord - min_v) / (max_v - min_v) if (max_v - min_v) > 0 else 0
    u2_norm = (u2 - min_u) / (max_u - min_u) if (max_u - min_u) > 0 else 0
    v2_norm = (v2_coord - min_v) / (max_v - min_v) if (max_v - min_v) > 0 else 0

    x1_mm = v1_norm * base_w
    y1_mm = u1_norm * base_h
    x2_mm = v2_norm * base_w
    y2_mm = u2_norm * base_h

    # Convert to page coordinates (with offset)
    x1_pt = template_x + (base_offset_x + x1_mm) * mm
    y1_pt = template_y + (base_offset_y + y1_mm) * mm
    x2_pt = template_x + (base_offset_x + x2_mm) * mm
    y2_pt = template_y + (base_offset_y + y2_mm) * mm

    c.line(x1_pt, y1_pt, x2_pt, y2_pt)

# Draw WRAP LAYER outline (red - CUTTING LINE)
print("Drawing wrap layer outline...")
c.setStrokeColor(red)
c.setLineWidth(2.0)

for edge in boundary_edges:
    v1, v2 = edge
    u1, v1_coord = v1
    u2, v2_coord = v2

    # Normalize and map to wrap layer dimensions
    u1_norm = (u1 - min_u) / (max_u - min_u) if (max_u - min_u) > 0 else 0
    v1_norm = (v1_coord - min_v) / (max_v - min_v) if (max_v - min_v) > 0 else 0
    u2_norm = (u2 - min_u) / (max_u - min_u) if (max_u - min_u) > 0 else 0
    v2_norm = (v2_coord - min_v) / (max_v - min_v) if (max_v - min_v) > 0 else 0

    x1_mm = v1_norm * wrap_w
    y1_mm = u1_norm * wrap_h
    x2_mm = v2_norm * wrap_w
    y2_mm = u2_norm * wrap_h

    # Convert to page coordinates
    x1_pt = template_x + x1_mm * mm
    y1_pt = template_y + y1_mm * mm
    x2_pt = template_x + x2_mm * mm
    y2_pt = template_y + y2_mm * mm

    c.line(x1_pt, y1_pt, x2_pt, y2_pt)

c.setStrokeColor(black)

# Dimensions
c.setFont("Helvetica", 8)

# Width dimension
dim_y = template_y - 10*mm
c.setStrokeColor(red)
c.line(template_x, dim_y, template_x + wrap_w * mm, dim_y)
c.line(template_x, dim_y - 2*mm, template_x, dim_y + 2*mm)
c.line(template_x + wrap_w * mm, dim_y - 2*mm, template_x + wrap_w * mm, dim_y + 2*mm)
c.setFillColor(red)
c.drawCentredString(template_x + wrap_w * mm / 2, dim_y - 6*mm,
                    f"{wrap_w:.1f} mm (with {overlap:.0f}mm overlap)")
c.setFillColor(black)
c.setStrokeColor(black)

# Height dimension
dim_x = template_x + wrap_w * mm + 5*mm
c.setStrokeColor(red)
c.line(dim_x, template_y, dim_x, template_y + wrap_h * mm)
c.line(dim_x - 2*mm, template_y, dim_x + 2*mm, template_y)
c.line(dim_x - 2*mm, template_y + wrap_h * mm, dim_x + 2*mm, template_y + wrap_h * mm)
c.saveState()
c.translate(dim_x + 3*mm, template_y + wrap_h * mm / 2)
c.rotate(90)
c.setFont("Helvetica", 7)
c.setFillColor(red)
c.drawCentredString(0, 0, f"{wrap_h:.1f} mm")
c.restoreState()
c.setFillColor(black)
c.setStrokeColor(black)

# Scale bar
scale_x = margin
scale_y = margin
scale_len = 100 * mm

c.setLineWidth(1.5)
c.rect(scale_x, scale_y, scale_len, 10*mm)
c.setFillColor(black)
c.rect(scale_x, scale_y, scale_len/2, 10*mm, fill=1, stroke=0)
c.setFillColor(black)

c.setLineWidth(1)
c.line(scale_x, scale_y, scale_x, scale_y - 5*mm)
c.line(scale_x + scale_len/2, scale_y, scale_x + scale_len/2, scale_y - 5*mm)
c.line(scale_x + scale_len, scale_y, scale_x + scale_len, scale_y - 5*mm)

c.setFont("Helvetica", 8)
c.drawString(scale_x, scale_y - 10*mm, "0")
c.drawString(scale_x + scale_len/2 - 10*mm, scale_y - 10*mm, "50mm")
c.drawString(scale_x + scale_len - 18*mm, scale_y - 10*mm, "100mm")

c.setFont("Helvetica-Bold", 9)
c.drawString(scale_x + scale_len + 5*mm, scale_y + 3*mm, "← MUST MEASURE 100mm EXACTLY")

# Legend
legend_x = page_w - margin - 125*mm
legend_y = template_y

c.setFont("Helvetica-Bold", 9)
c.drawString(legend_x, legend_y + wrap_h * mm + 5*mm, "TEMPLATE OUTLINES:")

c.setStrokeColor(blue)
c.setLineWidth(2)
c.line(legend_x, legend_y + wrap_h * mm - 3*mm, legend_x + 20*mm, legend_y + wrap_h * mm - 3*mm)
c.setStrokeColor(black)
c.setFont("Helvetica", 7)
c.drawString(legend_x + 22*mm, legend_y + wrap_h * mm - 5*mm, f"Base pipe: {base_w:.0f}×{base_h:.0f}mm (reference)")

c.setStrokeColor(red)
c.setLineWidth(2)
c.line(legend_x, legend_y + wrap_h * mm - 13*mm, legend_x + 20*mm, legend_y + wrap_h * mm - 13*mm)
c.setStrokeColor(black)
c.drawString(legend_x + 22*mm, legend_y + wrap_h * mm - 15*mm, f"Wrap layer: {wrap_w:.0f}×{wrap_h:.0f}mm")

# Footer
c.setFont("Helvetica", 7)
c.drawString(margin, 5*mm,
             "Print: 100% scale | Landscape | A4 | Verify scale bar | Cut along RED outline")

# Save
c.showPage()
c.save()

print(f"\n✓ PDF created: {pdf_path}")
print(f"✓ Base pipe outline: {base_w:.1f}mm × {base_h:.1f}mm (blue)")
print(f"✓ Wrap layer outline: {wrap_w:.1f}mm × {wrap_h:.1f}mm (RED - cutting line)")
print(f"✓ Actual UV unwrap shape - {len(boundary_edges)} edge segments")
print(f"\nCUT ALONG RED OUTLINE")
