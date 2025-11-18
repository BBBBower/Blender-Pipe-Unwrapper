================================================================================
EXHAUST WRAP FLAT PATTERN TEMPLATES
3" OD, 1.5D 90° Bend, 5 Segments
================================================================================

NEW: BLENDER ADDON AVAILABLE!
  For custom pipe specifications (any OD, radius, angle), use the Blender addon:
  - File: pipe_template_generator.py
  - Documentation: ADDON_INSTALLATION_GUIDE.txt
  - Generates templates for ANY pipe specification with GUI interface

QUICK START (Using Existing Template):
  1. Open: exhaust_wrap_template.pdf
  2. Print at 100% scale (Actual Size)
  3. Verify scale bar measures exactly 100mm
  4. Cut along RED outline
  5. Make 5 pieces for fiberglass, 5 for stainless

================================================================================
FILES IN THIS FOLDER:
================================================================================

BLENDER ADDON (NEW - RECOMMENDED):
  pipe_template_generator.py
    - Complete Blender addon with GUI interface
    - Generate templates for ANY pipe specification
    - Automatically creates 3D model, UV unwraps, and exports PDF
    - See ADDON_INSTALLATION_GUIDE.txt for installation and usage

MAIN TEMPLATE:
  exhaust_wrap_template.pdf
    - Final cutting template (ready to print)
    - Shows actual UV unwrap shape from Blender
    - Blue outline = base pipe (reference)
    - RED outline = cutting line for wrap materials
    - Two templates per page for efficiency

LEGACY REGENERATION SCRIPT:
  generate_pdf.py
    - Standalone Python script to regenerate PDF (legacy method)
    - Requires: reportlab library (pip install reportlab)
    - Run: python generate_pdf.py
    - Uses data from JSON files below (fixed dimensions)

DATA FILES:
  pdf_data.json
    - Template dimensions and specifications
    - Pipe OD, bend radius, segment angles
    - Wrap layer dimensions

  uv_data.json
    - UV unwrap polygon data from Blender
    - Contains 384 polygons from UV unwrap

  boundary_data.json
    - Boundary edge data (88 edges)
    - Used to draw clean outline on template

DOCUMENTATION:
  FINAL_PRINTING_GUIDE.txt
    - Complete printing and assembly instructions
    - Troubleshooting tips
    - Scale verification steps

  3INCH_5SEGMENT_CUTTING_GUIDE.txt
    - Detailed cutting dimensions
    - Material specifications
    - Assembly instructions

  SEGMENTED_BEND_CUTTING_GUIDE.md
    - Technical guide for segmented bends
    - Calculations explained

  COMPLETE_SOLUTION_SUMMARY.md
    - Original project summary
    - Background and context

================================================================================
SPECIFICATIONS:
================================================================================

Pipe:
  - Outer Diameter: 76.2mm (3 inches)
  - Material: Exhaust pipe

Bend:
  - Radius: 1.5D (114.3mm centerline)
  - Total Angle: 90°
  - Segments: 5 pieces @ 18° each

Wrap Materials:
  - Fiberglass: 6.0mm thick insulation
  - Stainless Steel: 0.15mm thick (304 embossed)
  - Overlap: 10mm (seam and segment joins)

Template Dimensions (at radius 43.6mm):
  - Width: 283.9mm
  - Length: 37.6mm
  - Quantity: 5 pieces each (fiberglass and stainless)

Split Line Location:
  - Inside of bend radius (concave side)
  - Longitudinal (along pipe length)
  - 10mm overlap included

================================================================================
PRINTING INSTRUCTIONS:
================================================================================

1. OPEN PDF:
   Open exhaust_wrap_template.pdf in Adobe Reader or PDF viewer

2. PRINT SETTINGS (CRITICAL):
   - Scale: 100% (Actual Size / Do Not Scale)
   - Orientation: Landscape
   - Paper: A4 (297mm × 210mm)
   - Margins: Minimum or None

3. VERIFY SCALE:
   - Measure the scale bar at bottom left
   - Must measure EXACTLY 100mm
   - If not, adjust printer settings and reprint

4. CUT:
   - Cut along RED outline
   - Make 5 identical pieces

================================================================================
ASSEMBLY:
================================================================================

For each segment:
  1. Wrap fiberglass first (284mm × 38mm)
  2. Position seam on INSIDE of bend (concave side)
  3. Ensure 10mm overlap
  4. Wrap stainless second (284mm × 38mm)
  5. Position seam on INSIDE of bend
  6. Ensure 10mm overlap

Connect all 5 wrapped segments end-to-end to form complete 90° elbow.
Each segment-to-segment join has 10mm overlap included.

================================================================================
REGENERATING THE TEMPLATE:
================================================================================

If you need to regenerate or modify the template:

1. Install Python and reportlab:
   pip install reportlab

2. Run the script:
   python generate_pdf.py

3. The script reads from:
   - pdf_data.json (dimensions)
   - boundary_data.json (UV outline)

4. Outputs:
   - exhaust_wrap_template.pdf (overwrites existing)

To modify dimensions:
  - Edit pdf_data.json
  - Change wrap_width, wrap_arc_length, or overlap values
  - Re-run generate_pdf.py

================================================================================
BLENDER SOURCE:
================================================================================

The template was generated from a Blender UV unwrap of a 3D curved pipe segment.

The seam was manually marked on the inside of the bend radius, then the pipe
was UV unwrapped to create the flat pattern shape.

The boundary edges (88 segments) represent the outer edge of the UV unwrap,
scaled to the appropriate dimensions for the wrap materials.

================================================================================
NOTES:
================================================================================

- All 5 segments are identical in size
- Template shows the curved/shaped outline from UV unwrap (not a rectangle)
- The shape accounts for pipe curvature and bend geometry
- Cut to RED outline for both fiberglass and stainless (same size)
- Template is optimized for 10mm overlap (seam and joins)

================================================================================
Generated: 2025-11-18
Project: Bower Motorsport
Status: READY FOR PRODUCTION
================================================================================
