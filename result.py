
"When I mention stacking two objects, 
it means that the second object is positioned directly on top of the first, with both objects sharing the same x and y coordinates. 
The z-coordinate of the second object is offset by half its thickness relative to the first object top position."
selection = mf.get_selection()
if len(selection) < 2:
    print("Select at least two objects")
else:
    first_obj_path = selection[0]
    second_obj_path = selection[1]
    first_obj_bbox = mf.get_bbox_world(stage, first_obj_path, Usd.TimeCode.Default())
    second_obj_bbox = mf.get_bbox_world(stage, second_obj_path, Usd.TimeCode.Default())
    z_pos = first_obj_bbox.GetMax()[2] + 0.5 * (second_obj_bbox.GetMax()[2] - second_obj_bbox.GetMin()[2])
    first_obj_translate = mf.get_translate(stage, first_obj_path)
    mf.set_translate(stage, second_obj_path, (first_obj_translate[0], first_obj_translate[1], z_pos))


selection = mf.get_selection()
if len(selection) != 3:
    print("Please select exactly three objects.")
else:
    prim1_path, prim2_path, prim3_path = selection
    bbox1 = mf.get_bbox_world(stage, prim1_path, Usd.TimeCode.Default())
    bbox2 = mf.get_bbox_world(stage, prim2_path, Usd.TimeCode.Default())
    bbox3 = mf.get_bbox_world(stage, prim3_path, Usd.TimeCode.Default())
    
    z_offset1 = bbox1.GetMax()[2] + 0.5 * (bbox2.GetMax()[2] - bbox2.GetMin()[2])
    translate1 = mf.get_translate(stage, prim1_path)
    mf.set_translate(stage, prim2_path, (translate1[0], translate1[1], z_offset1))
    
    z_offset2 = bbox2.GetMax()[2] + 0.5 * (bbox3.GetMax()[2] - bbox3.GetMin()[2])
    mf.set_translate(stage, prim3_path, (translate1[0], translate1[1], z_offset2))
