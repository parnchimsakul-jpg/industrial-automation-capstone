import adsk.core, adsk.fusion, traceback

def create_machine_box(rootComp, name, length_cm, width_cm, height_cm, pos_x_cm, pos_y_cm, color_rgb=(200, 200, 200)):
    """
    Creates an SMT machine bounding-box component in Fusion 360.
    Dimensions in cm (Fusion 360 internal unit is cm).
    """
    # Create new component occurrence
    occurrence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    comp = occurrence.component
    comp.name = name
    
    # Create sketch on XY plane
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    sketch = sketches.add(xyPlane)
    
    # Draw base rectangle centered or offset
    lines = sketch.sketchCurves.sketchLines
    x0 = pos_x_cm
    y0 = pos_y_cm
    x1 = pos_x_cm + length_cm
    y1 = pos_y_cm + width_cm
    
    recLines = lines.addTwoPointRectangle(
        adsk.core.Point3D.create(x0, y0, 0),
        adsk.core.Point3D.create(x1, y1, 0)
    )
    
    # Extrude
    prof = sketch.profiles.item(0)
    extrudes = comp.features.extrudeFeatures
    extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    distance = adsk.core.ValueInput.createByReal(height_cm)
    extInput.setDistanceExtent(False, distance)
    extrudes.add(extInput)
    
    # Track indicator cut/color (at standard rail height ~90cm from base)
    if height_cm >= 95.0:
        # Create a visual conveyor rail slit/channel at height 90cm
        xzPlane = comp.xZConstructionPlane
        trackSketch = sketches.add(xzPlane)
        trackLines = trackSketch.sketchCurves.sketchLines
        trackLines.addTwoPointRectangle(
            adsk.core.Point3D.create(x0, 89.0, 0),
            adsk.core.Point3D.create(x1, 91.0, 0)
        )
    return comp

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        if not design:
            ui.messageBox('Please open a new Fusion 360 design document first.')
            return

        rootComp = design.rootComponent

        # SMT Production Line Sequence (Dimensions in mm -> converted to cm)
        # Standard conveyor rail line runs along X axis
        machines = [
            # Name, Length (cm), Width (cm), Height (cm), Gap after (cm)
            ("01_ZB2535SBJ_Auto_Loader",      65.0,  80.0, 125.0,  5.0),
            ("02_ZB-4535LYS_Paste_Printer",   110.0, 95.0, 150.0,  5.0),
            ("03_Link_Conveyor_1",            60.0,  60.0,  92.0,  5.0),
            ("04_WS-8Y_Pick_and_Place",       135.0, 115.0, 145.0,  5.0),
            ("05_Link_Conveyor_2",            60.0,  60.0,  92.0,  5.0),
            ("06_ZBRF-835_Reflow_Oven",       272.0, 82.0, 136.0,  5.0),
            ("07_Link_Conveyor_3",            60.0,  60.0,  92.0,  5.0),
            ("08_ZB-800A_2D_AOI",             90.0,  85.0, 145.0,  5.0),
            ("09_Delta_SCARA_Dispenser",      80.0,  80.0, 140.0,  5.0),
            ("10_ZB2535XBJ_Auto_Unloader",    65.0,  80.0, 125.0,  0.0),
        ]

        current_x = 0.0
        for m_name, length, width, height, gap in machines:
            create_machine_box(rootComp, m_name, length, width, height, current_x, 0.0)
            current_x += (length + gap)

        ui.messageBox(f'Successfully generated entire SMT Line CAD layout!\nTotal Length: {current_x*10:.0f} mm')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
