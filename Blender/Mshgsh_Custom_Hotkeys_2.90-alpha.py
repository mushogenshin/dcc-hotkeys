keyconfig_data = [
    (
        "3D View",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "view3d.cursor3d",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_panel",
                    {"type": "RET", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "TOPBAR_PT_name"),
                            ("keep_open", False),
                        ],
                    },
                ),
                (
                    "wm.search_menu",
                    {"type": "SPACE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "view3d.localview",
                    {"type": "I", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "V", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_view_pie"),
                        ],
                    },
                ),
                (
                    "view3d.rotate",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "view3d.move",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "view3d.zoom",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "view3d.view_selected",
                    {"type": "F", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                        ],
                    },
                ),
                (
                    "view3d.view_selected",
                    {"type": "F", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_all_regions", False),
                        ],
                    },
                ),
                (
                    "view3d.smoothview",
                    {"type": "TIMER1", "value": "ANY", "any": True},
                    None,
                ),
                ("view3d.rotate", {"type": "TRACKPADPAN", "value": "ANY"}, None),
                ("view3d.rotate", {"type": "MOUSEROTATE", "value": "ANY"}, None),
                (
                    "view3d.move",
                    {"type": "TRACKPADPAN", "value": "ANY", "shift": True},
                    None,
                ),
                ("view3d.zoom", {"type": "TRACKPADZOOM", "value": "ANY"}, None),
                (
                    "view3d.zoom",
                    {"type": "TRACKPADPAN", "value": "ANY", "ctrl": True},
                    None,
                ),
                (
                    "view3d.zoom",
                    {"type": "NUMPAD_PLUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "NUMPAD_MINUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "WHEELINMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "WHEELOUTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "WHEELINMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "WHEELOUTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.view_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("center", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "view3d.view_all",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                            ("center", False),
                        ],
                        "active": False,
                    },
                ),
                ("view3d.view_camera", {"type": "F4", "value": "PRESS"}, None),
                (
                    "view3d.view_axis",
                    {"type": "F1", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FRONT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "F2", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "F3", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "TOP"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "F1", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "BACK"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "F2", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "F3", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                        ],
                    },
                ),
                (
                    "view3d.view_orbit",
                    {"type": "F5", "value": "PRESS"},
                    {
                        "properties": [
                            ("angle", 3.1415927),
                            ("type", "ORBITRIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.ndof_orbit_zoom",
                    {"type": "NDOF_MOTION", "value": "ANY"},
                    None,
                ),
                (
                    "view3d.ndof_orbit",
                    {"type": "NDOF_MOTION", "value": "ANY", "ctrl": True},
                    None,
                ),
                (
                    "view3d.ndof_pan",
                    {"type": "NDOF_MOTION", "value": "ANY", "shift": True},
                    None,
                ),
                (
                    "view3d.ndof_all",
                    {
                        "type": "NDOF_MOTION",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                (
                    "view3d.view_selected",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_all_regions", False),
                        ],
                    },
                ),
                (
                    "view3d.view_roll",
                    {"type": "NDOF_BUTTON_ROLL_CCW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_roll",
                    {"type": "NDOF_BUTTON_ROLL_CCW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_FRONT", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FRONT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_BACK", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "BACK"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_LEFT", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_RIGHT", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_TOP", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "TOP"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_BOTTOM", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_FRONT", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "FRONT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_RIGHT", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_TOP", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "TOP"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("center", True),
                            ("object", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("toggle", True),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("toggle", True),
                            ("enumerate", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                            ("center", True),
                            ("enumerate", True),
                        ],
                    },
                ),
                (
                    "view3d.zoom_border",
                    {"type": "Z", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "view3d.copybuffer",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "view3d.pastebuffer",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "view3d.toggle_xray",
                    {"type": "ONE", "value": "PRESS", "shift": True},
                    None,
                ),
                ("view3d.object_as_camera", {"type": "L", "value": "PRESS"}, None),
                ("view3d.view_persportho", {"type": "P", "value": "PRESS"}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "X", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_snap_pie"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "E", "value": "PRESS"}, None),
                ("transform.resize", {"type": "R", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_pivot_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "COMMA", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_orientations_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_snap"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Generic",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "LEFT_BRACKET", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_toolbar"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "RIGHT_BRACKET", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Cursor",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Bend",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.bend",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.bend",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Extrude",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("gpencil.extrude_move", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("gpencil.extrude_move", {"type": "EVT_TWEAK_M", "value": "ANY"}, None),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Radius",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.transform",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "GPENCIL_SHRINKFATTEN"),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "GPENCIL_SHRINKFATTEN"),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Select Box",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("gpencil.select_box", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "gpencil.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "gpencil.select_box",
                    {
                        "type": "EVT_TWEAK_L",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "AND"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Select Circle",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                            ("mode", "SUB"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Select Lasso",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("gpencil.select_lasso", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {
                        "type": "EVT_TWEAK_L",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "AND"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Shear",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, To Sphere",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.tosphere",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.tosphere",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Edit Gpencil, Tweak",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Arc",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "ARC"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "ARC"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "ARC"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "ARC"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "ARC"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "ARC"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Box",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "BOX"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "BOX"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "BOX"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "BOX"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "BOX"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "BOX"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Circle",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "CIRCLE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "CIRCLE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "CIRCLE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "CIRCLE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "CIRCLE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "CIRCLE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Curve",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "CURVE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "CURVE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Cutter",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.stroke_cutter",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "gpencil.stroke_cutter",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Eyedropper",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "ui.eyedropper_gpencil_color",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "ui.eyedropper_gpencil_color",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "ui.eyedropper_gpencil_color",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                (
                    "ui.eyedropper_gpencil_color",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "ui.eyedropper_gpencil_color",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "ui.eyedropper_gpencil_color",
                    {
                        "type": "MIDDLEMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Line",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "LINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "LINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "LINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "LINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "LINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("type", "LINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Gpencil, Polyline",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "POLYLINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "POLYLINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "gpencil.primitive",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("type", "POLYLINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.primitive",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "POLYLINE"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Weight, Gradient",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "paint.weight_gradient",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
                (
                    "paint.weight_gradient",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Weight, Sample Vertex Group",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "paint.weight_sample_group",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "paint.weight_sample_group",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Paint Weight, Sample Weight",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("paint.weight_sample", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "paint.weight_sample",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    None,
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt Gpencil, Paint",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt Gpencil, Select Box",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("gpencil.select_box", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "gpencil.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "gpencil.select_box",
                    {
                        "type": "EVT_TWEAK_L",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "AND"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt Gpencil, Select Circle",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                            ("mode", "SUB"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt Gpencil, Select Lasso",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("gpencil.select_lasso", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {
                        "type": "EVT_TWEAK_L",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "AND"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt Gpencil, Tweak",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt, Box Hide",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "paint.hide_show",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("action", "HIDE"),
                        ],
                    },
                ),
                (
                    "paint.hide_show",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SHOW"),
                        ],
                    },
                ),
                (
                    "paint.hide_show",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SHOW"),
                            ("area", "ALL"),
                        ],
                    },
                ),
                (
                    "paint.hide_show",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("action", "HIDE"),
                        ],
                    },
                ),
                (
                    "paint.hide_show",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SHOW"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt, Box Mask",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "view3d.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "view3d.select_box",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_box",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt, Lasso Mask",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "paint.mask_lasso_gesture",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("value", 1.0),
                        ],
                    },
                ),
                (
                    "paint.mask_lasso_gesture",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("value", 0.0),
                        ],
                    },
                ),
                (
                    "paint.mask_lasso_gesture",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("value", 1.0),
                        ],
                    },
                ),
                (
                    "paint.mask_lasso_gesture",
                    {"type": "EVT_TWEAK_M", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("value", 0.0),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Sculpt, Mesh Filter",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("sculpt.mesh_filter", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("sculpt.mesh_filter", {"type": "EVT_TWEAK_M", "value": "ANY"}, None),
            ],
        },
    ),
    (
        "3D View Tool: Select Box",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("view3d.select_box", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "view3d.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "view3d.select_box",
                    {
                        "type": "EVT_TWEAK_L",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "AND"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Select Circle",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "view3d.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "view3d.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_circle",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                            ("mode", "SUB"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Select Lasso",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("view3d.select_lasso", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "view3d.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "view3d.select_lasso",
                    {
                        "type": "EVT_TWEAK_L",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "AND"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Shear",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_L", "value": "NORTH"},
                    {
                        "properties": [
                            ("orient_axis_ortho", "Y"),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_L", "value": "SOUTH"},
                    {
                        "properties": [
                            ("orient_axis_ortho", "Y"),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("orient_axis_ortho", "X"),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_M", "value": "NORTH"},
                    {
                        "properties": [
                            ("orient_axis_ortho", "Y"),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_M", "value": "SOUTH"},
                    {
                        "properties": [
                            ("orient_axis_ortho", "Y"),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.shear",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("orient_axis_ortho", "X"),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Transform",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("transform.from_gizmo", {"type": "EVT_TWEAK_M", "value": "ANY"}, None),
            ],
        },
    ),
    (
        "3D View Tool: Tweak",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Animation",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "T", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_seconds"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Animation Channels",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("anim.channels_click", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "anim.channels_click",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "anim.channels_click",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("children_only", True),
                        ],
                    },
                ),
                ("anim.channels_rename", {"type": "RET", "value": "PRESS"}, None),
                (
                    "anim.channels_rename",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                (
                    "anim.channel_select_keys",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                (
                    "anim.channel_select_keys",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "anim.channels_find",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "anim.channels_select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "anim.channels_select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "anim.channels_select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                ("anim.channels_select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "anim.channels_select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
                (
                    "anim.channels_delete",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    None,
                ),
                ("anim.channels_delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "anim.channels_setting_toggle",
                    {"type": "W", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "anim.channels_setting_enable",
                    {"type": "W", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "anim.channels_setting_disable",
                    {"type": "W", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "anim.channels_editable_toggle",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                (
                    "anim.channels_expand",
                    {"type": "RIGHT_ARROW", "value": "PRESS"},
                    None,
                ),
                (
                    "anim.channels_collapse",
                    {"type": "LEFT_ARROW", "value": "PRESS"},
                    None,
                ),
                (
                    "anim.channels_expand",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                (
                    "anim.channels_collapse",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                (
                    "anim.channels_move",
                    {"type": "PAGE_UP", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "UP"),
                        ],
                    },
                ),
                (
                    "anim.channels_move",
                    {"type": "PAGE_DOWN", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "DOWN"),
                        ],
                    },
                ),
                (
                    "anim.channels_move",
                    {"type": "PAGE_UP", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "TOP"),
                        ],
                    },
                ),
                (
                    "anim.channels_move",
                    {"type": "PAGE_DOWN", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "BOTTOM"),
                        ],
                    },
                ),
                (
                    "anim.channels_group",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "anim.channels_ungroup",
                    {"type": "G", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "DOPESHEET_MT_channel_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "DOPESHEET_MT_channel_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Armature",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "armature.hide",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "armature.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                ("armature.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "armature.align",
                    {"type": "A", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "armature.calculate_roll",
                    {"type": "N", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "armature.roll_clear",
                    {"type": "R", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "armature.switch_direction",
                    {"type": "F", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "armature.bone_primitive_add",
                    {"type": "A", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "armature.parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "armature.parent_clear",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "armature.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "armature.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "armature.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "armature.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "armature.select_mirror",
                    {"type": "M", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "armature.select_hierarchy",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "PARENT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "armature.select_hierarchy",
                    {"type": "LEFT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "PARENT"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "armature.select_hierarchy",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "CHILD"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "armature.select_hierarchy",
                    {"type": "RIGHT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "CHILD"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "armature.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "armature.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "armature.select_similar",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "armature.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "armature.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    },
                ),
                (
                    "armature.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "armature.shortest_path_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_armature_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_armature_delete"),
                        ],
                    },
                ),
                (
                    "armature.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "armature.dissolve",
                    {"type": "X", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "armature.dissolve",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("armature.extrude_move", {"type": "U", "value": "PRESS"}, None),
                (
                    "armature.extrude_forked",
                    {"type": "U", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "armature.click_extrude",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "ctrl": True},
                    None,
                ),
                ("armature.fill", {"type": "F", "value": "PRESS"}, None),
                ("armature.split", {"type": "Y", "value": "PRESS"}, None),
                (
                    "armature.separate",
                    {"type": "P", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_bone_options_toggle"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_bone_options_enable"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_bone_options_disable"),
                        ],
                    },
                ),
                (
                    "armature.layers_show_all",
                    {"type": "ACCENT_GRAVE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "armature.armature_layers",
                    {"type": "M", "value": "PRESS", "shift": True},
                    None,
                ),
                ("armature.bone_layers", {"type": "M", "value": "PRESS"}, None),
                (
                    "transform.bbone_resize",
                    {"type": "S", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "transform.transform",
                    {"type": "S", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "BONE_ENVELOPE"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "R", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "BONE_ROLL"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_armature_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_armature_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Bevel Modal Map",
        {"space_type": "EMPTY", "region_type": "WINDOW", "modal": True},
        {
            "items": [
                ("CANCEL", {"type": "ESC", "value": "PRESS", "any": True}, None),
                ("CANCEL", {"type": "RIGHTMOUSE", "value": "PRESS", "any": True}, None),
                ("CONFIRM", {"type": "RET", "value": "PRESS", "any": True}, None),
                (
                    "CONFIRM",
                    {"type": "NUMPAD_ENTER", "value": "PRESS", "any": True},
                    None,
                ),
                ("CONFIRM", {"type": "LEFTMOUSE", "value": "PRESS", "any": True}, None),
                ("VALUE_OFFSET", {"type": "A", "value": "PRESS", "any": True}, None),
                (
                    "VALUE_PROFILE",
                    {"type": "P", "value": "PRESS", "any": True},
                    {
                        "active": False,
                    },
                ),
                ("VALUE_SEGMENTS", {"type": "S", "value": "PRESS", "any": True}, None),
                (
                    "SEGMENTS_UP",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "SEGMENTS_UP",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "SEGMENTS_DOWN",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "SEGMENTS_DOWN",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "OFFSET_MODE_CHANGE",
                    {"type": "M", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "CLAMP_OVERLAP_TOGGLE",
                    {"type": "C", "value": "PRESS", "any": True},
                    None,
                ),
                ("", {"type": "V", "value": "PRESS", "any": True}, None),
                (
                    "HARDEN_NORMALS_TOGGLE",
                    {"type": "H", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "MARK_SEAM_TOGGLE",
                    {"type": "U", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "MARK_SHARP_TOGGLE",
                    {"type": "K", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "OUTER_MITER_CHANGE",
                    {"type": "O", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "INNER_MITER_CHANGE",
                    {"type": "I", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "PROFILE_TYPE_CHANGE",
                    {"type": "Z", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "VERTEX_MESH_CHANGE",
                    {"type": "N", "value": "PRESS", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Clip",
        {"space_type": "CLIP_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_toolbar"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "N", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
                ("clip.open", {"type": "O", "value": "PRESS", "alt": True}, None),
                (
                    "clip.track_markers",
                    {"type": "LEFT_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("backwards", True),
                            ("sequence", False),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("backwards", False),
                            ("sequence", False),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {"type": "T", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("backwards", False),
                            ("sequence", True),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {"type": "T", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("backwards", True),
                            ("sequence", True),
                        ],
                    },
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": "TAB", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.mode"),
                            ("value_1", "TRACKING"),
                            ("value_2", "MASK"),
                        ],
                    },
                ),
                (
                    "clip.prefetch",
                    {"type": "P", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_tracking_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_solving_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "E", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_marker_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "W", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_reconstruction_pie"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Clip Editor",
        {"space_type": "CLIP_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                ("clip.view_pan", {"type": "MIDDLEMOUSE", "value": "PRESS"}, None),
                (
                    "clip.view_pan",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                ("clip.view_pan", {"type": "TRACKPADPAN", "value": "ANY"}, None),
                (
                    "clip.view_zoom",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("clip.view_zoom", {"type": "TRACKPADZOOM", "value": "ANY"}, None),
                (
                    "clip.view_zoom",
                    {"type": "TRACKPADPAN", "value": "ANY", "ctrl": True},
                    None,
                ),
                ("clip.view_zoom_in", {"type": "WHEELINMOUSE", "value": "PRESS"}, None),
                (
                    "clip.view_zoom_out",
                    {"type": "WHEELOUTMOUSE", "value": "PRESS"},
                    None,
                ),
                ("clip.view_zoom_in", {"type": "NUMPAD_PLUS", "value": "PRESS"}, None),
                (
                    "clip.view_zoom_out",
                    {"type": "NUMPAD_MINUS", "value": "PRESS"},
                    None,
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_1", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.5),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.25),
                        ],
                        "active": False,
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.125),
                        ],
                        "active": False,
                    },
                ),
                ("clip.view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "clip.view_all",
                    {"type": "F", "value": "PRESS"},
                    {
                        "properties": [
                            ("fit_view", True),
                        ],
                    },
                ),
                (
                    "clip.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                ("clip.view_all", {"type": "NDOF_BUTTON_FIT", "value": "PRESS"}, None),
                ("clip.view_ndof", {"type": "NDOF_MOTION", "value": "ANY"}, None),
                (
                    "clip.frame_jump",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHSTART"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHEND"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("position", "FAILEDPREV"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHSTART"),
                        ],
                    },
                ),
                ("clip.change_frame", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "clip.select",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "clip.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("clip.select_box", {"type": "B", "value": "PRESS"}, None),
                ("clip.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "wm.call_menu",
                    {"type": "G", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_select_grouped"),
                        ],
                    },
                ),
                (
                    "clip.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "clip.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "clip.add_marker_slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "clip.delete_marker",
                    {"type": "X", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "clip.delete_marker",
                    {"type": "DEL", "value": "PRESS", "shift": True},
                    None,
                ),
                ("clip.slide_marker", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "clip.disable_markers",
                    {"type": "D", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "TOGGLE"),
                        ],
                    },
                ),
                ("clip.delete_track", {"type": "X", "value": "PRESS"}, None),
                ("clip.delete_track", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "clip.lock_tracks",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "LOCK"),
                        ],
                    },
                ),
                (
                    "clip.lock_tracks",
                    {"type": "L", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "UNLOCK"),
                        ],
                    },
                ),
                (
                    "clip.hide_tracks",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "clip.hide_tracks",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "clip.hide_tracks_clear",
                    {"type": "H", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "clip.slide_plane_marker",
                    {"type": "LEFTMOUSE", "value": "CLICK_DRAG"},
                    None,
                ),
                ("clip.keyframe_insert", {"type": "I", "value": "PRESS"}, None),
                (
                    "clip.keyframe_delete",
                    {"type": "I", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "clip.join_tracks",
                    {"type": "J", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("clip.lock_selection_toggle", {"type": "L", "value": "PRESS"}, None),
                (
                    "wm.context_toggle",
                    {"type": "D", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_disabled"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "S", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_marker_search"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.use_mute_footage"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "REMAINED"),
                            ("clear_active", False),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "UPTO"),
                            ("clear_active", False),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("action", "ALL"),
                            ("clear_active", False),
                        ],
                    },
                ),
                (
                    "clip.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_pivot_pie"),
                        ],
                    },
                ),
                (
                    "clip.copy_tracks",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "clip.paste_tracks",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_tracking_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_tracking_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Clip Graph Editor",
        {"space_type": "CLIP_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "clip.graph_select",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "clip.graph_select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("clip.graph_select_box", {"type": "B", "value": "PRESS"}, None),
                ("clip.graph_delete_curve", {"type": "X", "value": "PRESS"}, None),
                ("clip.graph_delete_curve", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "clip.graph_delete_knot",
                    {"type": "X", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "clip.graph_delete_knot",
                    {"type": "DEL", "value": "PRESS", "shift": True},
                    None,
                ),
                ("clip.graph_view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "clip.graph_view_all",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
                (
                    "clip.graph_center_current_frame",
                    {"type": "NUMPAD_0", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.lock_time_cursor"),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "REMAINED"),
                            ("clear_active", True),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "UPTO"),
                            ("clear_active", True),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("action", "ALL"),
                            ("clear_active", True),
                        ],
                    },
                ),
                (
                    "clip.graph_disable_markers",
                    {"type": "D", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "TOGGLE"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                (
                    "clip.change_frame",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Console",
        {"space_type": "CONSOLE", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "console.move",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                (
                    "console.move",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "console.move",
                    {"type": "HOME", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LINE_BEGIN"),
                        ],
                    },
                ),
                (
                    "console.move",
                    {"type": "END", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LINE_END"),
                        ],
                    },
                ),
                (
                    "wm.context_cycle_int",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", False),
                        ],
                    },
                ),
                (
                    "wm.context_cycle_int",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", True),
                        ],
                    },
                ),
                (
                    "wm.context_cycle_int",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", False),
                        ],
                    },
                ),
                (
                    "wm.context_cycle_int",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", True),
                        ],
                    },
                ),
                (
                    "console.move",
                    {"type": "LEFT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "console.move",
                    {"type": "RIGHT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_CHARACTER"),
                        ],
                    },
                ),
                (
                    "console.history_cycle",
                    {"type": "UP_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("reverse", True),
                        ],
                    },
                ),
                (
                    "console.history_cycle",
                    {"type": "DOWN_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("reverse", False),
                        ],
                    },
                ),
                (
                    "console.delete",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_CHARACTER"),
                        ],
                    },
                ),
                (
                    "console.delete",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "console.delete",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "console.delete",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "console.delete",
                    {"type": "BACK_SPACE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                (
                    "console.clear_line",
                    {"type": "RET", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "console.clear_line",
                    {"type": "NUMPAD_ENTER", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "console.execute",
                    {"type": "RET", "value": "PRESS"},
                    {
                        "properties": [
                            ("interactive", True),
                        ],
                    },
                ),
                (
                    "console.execute",
                    {"type": "NUMPAD_ENTER", "value": "PRESS"},
                    {
                        "properties": [
                            ("interactive", True),
                        ],
                    },
                ),
                (
                    "console.copy_as_script",
                    {"type": "C", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                ("console.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                ("console.paste", {"type": "V", "value": "PRESS", "ctrl": True}, None),
                ("console.select_set", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "console.select_word",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                (
                    "console.insert",
                    {"type": "TAB", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("text", "\t"),
                        ],
                    },
                ),
                (
                    "console.indent_or_autocomplete",
                    {"type": "TAB", "value": "PRESS"},
                    None,
                ),
                (
                    "console.unindent",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CONSOLE_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CONSOLE_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "console.insert",
                    {"type": "TEXTINPUT", "value": "ANY", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Curve",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "TOPBAR_MT_edit_curve_add"),
                        ],
                    },
                ),
                ("curve.handle_type_set", {"type": "V", "value": "PRESS"}, None),
                (
                    "curve.vertex_add",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "ctrl": True},
                    None,
                ),
                (
                    "curve.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "curve.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "curve.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "curve.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "curve.select_row",
                    {"type": "R", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "curve.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "curve.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "curve.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "curve.select_similar",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "curve.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "curve.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    },
                ),
                (
                    "curve.shortest_path_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    None,
                ),
                (
                    "curve.separate",
                    {"type": "P", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                ("curve.split", {"type": "Y", "value": "PRESS"}, None),
                ("curve.extrude_move", {"type": "U", "value": "PRESS"}, None),
                (
                    "curve.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                ("curve.make_segment", {"type": "F", "value": "PRESS"}, None),
                (
                    "curve.cyclic_toggle",
                    {"type": "C", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_curve_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_curve_delete"),
                        ],
                    },
                ),
                (
                    "curve.dissolve_verts",
                    {"type": "X", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "curve.dissolve_verts",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "curve.tilt_clear",
                    {"type": "T", "value": "PRESS", "alt": True},
                    None,
                ),
                ("transform.tilt", {"type": "T", "value": "PRESS", "ctrl": True}, None),
                (
                    "transform.transform",
                    {"type": "S", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "CURVE_SHRINKFATTEN"),
                        ],
                    },
                ),
                ("curve.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "curve.hide",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "curve.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "curve.normals_make_consistent",
                    {"type": "N", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "object.vertex_parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_hook"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_connected"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_curve_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_curve_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Dopesheet",
        {"space_type": "DOPESHEET_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "screen.frame_offset",
                    {"type": "X", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "screen.frame_offset",
                    {"type": "C", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("end", True),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("end", False),
                        ],
                    },
                ),
                (
                    "action.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect_all", True),
                            ("column", False),
                            ("channel", False),
                        ],
                    },
                ),
                (
                    "action.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", True),
                            ("channel", False),
                        ],
                    },
                ),
                (
                    "action.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("channel", False),
                        ],
                    },
                ),
                (
                    "action.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", True),
                            ("channel", False),
                        ],
                    },
                ),
                (
                    "action.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", False),
                            ("channel", True),
                        ],
                    },
                ),
                (
                    "action.clickselect",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("channel", True),
                        ],
                    },
                ),
                (
                    "action.select_leftright",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "CHECK"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "action.select_leftright",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "LEFT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "action.select_leftright",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "RIGHT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "action.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "action.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "action.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "action.select_box",
                    {"type": "Q", "value": "PRESS"},
                    {
                        "properties": [
                            ("axis_range", False),
                        ],
                    },
                ),
                (
                    "action.select_box",
                    {"type": "Q", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                        ],
                    },
                ),
                (
                    "action.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("wait_for_input", False),
                            ("mode", "SET"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "action.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("wait_for_input", False),
                            ("mode", "ADD"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "action.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("wait_for_input", False),
                            ("mode", "SUB"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "action.select_column",
                    {"type": "K", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "KEYS"),
                        ],
                    },
                ),
                (
                    "action.select_column",
                    {"type": "K", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "CFRA"),
                        ],
                    },
                ),
                (
                    "action.select_column",
                    {"type": "K", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "MARKERS_COLUMN"),
                        ],
                    },
                ),
                (
                    "action.select_column",
                    {"type": "K", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "MARKERS_BETWEEN"),
                        ],
                    },
                ),
                (
                    "action.select_more",
                    {"type": "UP_ARROW", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "action.select_less",
                    {"type": "DOWN_ARROW", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "action.select_linked",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "action.frame_jump",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.context_menu_enum",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.auto_snap"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "X", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "DOPESHEET_MT_snap_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "DOPESHEET_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "DOPESHEET_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "DOPESHEET_MT_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "DOPESHEET_MT_delete"),
                        ],
                    },
                ),
                (
                    "action.duplicate_move",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("action.keyframe_insert", {"type": "S", "value": "PRESS"}, None),
                ("action.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                ("action.paste", {"type": "V", "value": "PRESS", "ctrl": True}, None),
                (
                    "action.paste",
                    {"type": "V", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    },
                ),
                (
                    "action.previewrange_set",
                    {"type": "P", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "active": False,
                    },
                ),
                ("action.view_all", {"type": "A", "value": "PRESS"}, None),
                (
                    "action.view_all",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
                ("action.view_selected", {"type": "F", "value": "PRESS"}, None),
                ("action.view_frame", {"type": "NUMPAD_0", "value": "PRESS"}, None),
                (
                    "anim.channels_editable_toggle",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                (
                    "anim.channels_find",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "transform.transform",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_TRANSLATE"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "TIME_TRANSLATE"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "TIME_TRANSLATE"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_EXTEND"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "R", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_SCALE"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "T", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "TIME_SLIDE"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_action"),
                        ],
                    },
                ),
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                ("marker.rename", {"type": "RET", "value": "PRESS"}, None),
                (
                    "anim.start_frame_set",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "anim.end_frame_set",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Dopesheet Generic",
        {"space_type": "DOPESHEET_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.call_panel",
                    {"type": "RET", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "TOPBAR_PT_name"),
                            ("keep_open", False),
                        ],
                    },
                ),
                ("wm.search_menu", {"type": "TAB", "value": "PRESS"}, None),
                (
                    "wm.context_toggle",
                    {"type": "RIGHT_BRACKET", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "File Browser",
        {"space_type": "FILE_BROWSER", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "file.parent",
                    {"type": "UP_ARROW", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "file.parent",
                    {"type": "UP_ARROW", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "file.previous",
                    {"type": "LEFT_ARROW", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "file.previous",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "file.next",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "file.next",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("file.refresh", {"type": "R", "value": "PRESS", "ctrl": True}, None),
                ("file.previous", {"type": "BACK_SPACE", "value": "PRESS"}, None),
                (
                    "file.next",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.params.show_hidden"),
                        ],
                    },
                ),
                (
                    "file.directory_new",
                    {"type": "I", "value": "PRESS"},
                    {
                        "properties": [
                            ("confirm", False),
                        ],
                    },
                ),
                ("file.rename", {"type": "F2", "value": "PRESS"}, None),
                ("file.delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "file.smoothscroll",
                    {"type": "TIMER1", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_toolbar"),
                        ],
                    },
                ),
                (
                    "file.bookmark_add",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_PLUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("increment", 1),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("increment", 10),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("increment", 100),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_MINUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("increment", -1),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("increment", -10),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("increment", -100),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "FILEBROWSER_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "FILEBROWSER_MT_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "File Browser Buttons",
        {"space_type": "FILE_BROWSER", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "file.filenum",
                    {"type": "NUMPAD_PLUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("increment", 1),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("increment", 10),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("increment", 100),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_MINUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("increment", -1),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("increment", -10),
                        ],
                    },
                ),
                (
                    "file.filenum",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("increment", -100),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "File Browser Main",
        {"space_type": "FILE_BROWSER", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "file.execute",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("need_active", True),
                        ],
                    },
                ),
                ("file.refresh", {"type": "R", "value": "PRESS", "ctrl": True}, None),
                ("file.select", {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"}, None),
                (
                    "file.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("open", False),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "file.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "file.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("fill", True),
                            ("open", False),
                        ],
                    },
                ),
                (
                    "file.select",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("open", False),
                        ],
                    },
                ),
                (
                    "file.select",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("fill", True),
                            ("open", False),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "UP_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "UP"),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "UP_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "UP"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "UP_ARROW", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", "UP"),
                            ("extend", True),
                            ("fill", True),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "DOWN_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "DOWN"),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "DOWN_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "DOWN"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {
                        "type": "DOWN_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("direction", "DOWN"),
                            ("extend", True),
                            ("fill", True),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "LEFT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "LEFT"),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "LEFT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "LEFT"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("direction", "LEFT"),
                            ("extend", True),
                            ("fill", True),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "RIGHT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "RIGHT"),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "RIGHT"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "file.select_walk",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("direction", "RIGHT"),
                            ("extend", True),
                            ("fill", True),
                        ],
                    },
                ),
                ("file.previous", {"type": "BUTTON4MOUSE", "value": "CLICK"}, None),
                ("file.next", {"type": "BUTTON5MOUSE", "value": "CLICK"}, None),
                (
                    "file.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("file.select_box", {"type": "Q", "value": "PRESS"}, None),
                ("file.select_box", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "file.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "file.highlight",
                    {"type": "MOUSEMOVE", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "file.sort_column_ui_context",
                    {"type": "LEFTMOUSE", "value": "PRESS", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Font",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "font.style_toggle",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("style", "BOLD"),
                        ],
                    },
                ),
                (
                    "font.style_toggle",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("style", "ITALIC"),
                        ],
                    },
                ),
                (
                    "font.style_toggle",
                    {"type": "U", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("style", "UNDERLINE"),
                        ],
                    },
                ),
                (
                    "font.style_toggle",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("style", "SMALL_CAPS"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "font.delete",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_OR_SELECTION"),
                        ],
                    },
                ),
                (
                    "font.delete",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "font.delete",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_OR_SELECTION"),
                        ],
                    },
                ),
                (
                    "font.delete",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_OR_SELECTION"),
                        ],
                    },
                ),
                (
                    "font.delete",
                    {"type": "BACK_SPACE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "HOME", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LINE_BEGIN"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "END", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LINE_END"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "LEFT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "RIGHT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_CHARACTER"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "UP_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_LINE"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "DOWN_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_LINE"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "PAGE_UP", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_PAGE"),
                        ],
                    },
                ),
                (
                    "font.move",
                    {"type": "PAGE_DOWN", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_PAGE"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "HOME", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "LINE_BEGIN"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "END", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "LINE_END"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "LEFT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "NEXT_CHARACTER"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "UP_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_LINE"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "DOWN_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "NEXT_LINE"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "PAGE_UP", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_PAGE"),
                        ],
                    },
                ),
                (
                    "font.move_select",
                    {"type": "PAGE_DOWN", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "NEXT_PAGE"),
                        ],
                    },
                ),
                (
                    "font.change_spacing",
                    {"type": "LEFT_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "font.change_spacing",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "font.change_character",
                    {"type": "UP_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "font.change_character",
                    {"type": "DOWN_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "font.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("font.text_copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                ("font.text_cut", {"type": "X", "value": "PRESS", "ctrl": True}, None),
                (
                    "font.text_paste",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("font.line_break", {"type": "RET", "value": "PRESS"}, None),
                (
                    "font.text_insert",
                    {"type": "TEXTINPUT", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "font.text_insert",
                    {"type": "BACK_SPACE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("accent", True),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_font_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_font_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Frames",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "screen.frame_jump",
                    {"type": "MEDIA_LAST", "value": "PRESS"},
                    {
                        "properties": [
                            ("end", True),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {"type": "MEDIA_FIRST", "value": "PRESS"},
                    {
                        "properties": [
                            ("end", False),
                        ],
                    },
                ),
                (
                    "screen.animation_play",
                    {"type": "V", "value": "PRESS", "alt": True},
                    None,
                ),
                ("screen.animation_cancel", {"type": "ESC", "value": "PRESS"}, None),
                (
                    "screen.animation_play",
                    {"type": "MEDIA_PLAY", "value": "PRESS"},
                    None,
                ),
                (
                    "screen.animation_cancel",
                    {"type": "MEDIA_STOP", "value": "PRESS"},
                    None,
                ),
                (
                    "screen.keyframe_jump",
                    {"type": "C", "value": "PRESS"},
                    {
                        "properties": [
                            ("next", True),
                        ],
                    },
                ),
                (
                    "screen.keyframe_jump",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("next", False),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Generic Gizmo",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gizmogroup.gizmo_tweak",
                    {"type": "LEFTMOUSE", "value": "PRESS", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Generic Gizmo Click Drag",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gizmogroup.gizmo_tweak",
                    {"type": "LEFTMOUSE", "value": "CLICK", "any": True},
                    None,
                ),
                (
                    "gizmogroup.gizmo_tweak",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Generic Gizmo Drag",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gizmogroup.gizmo_tweak",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
            ],
        },
    ),
    (
        "Generic Gizmo Maybe Drag",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gizmogroup.gizmo_tweak",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
            ],
        },
    ),
    (
        "Generic Gizmo Select",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gizmogroup.gizmo_tweak",
                    {"type": "LEFTMOUSE", "value": "PRESS", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Generic Gizmo Tweak Modal Map",
        {"space_type": "EMPTY", "region_type": "WINDOW", "modal": True},
        {
            "items": [
                ("CANCEL", {"type": "ESC", "value": "PRESS", "any": True}, None),
                ("CANCEL", {"type": "RIGHTMOUSE", "value": "PRESS", "any": True}, None),
                ("CONFIRM", {"type": "RET", "value": "PRESS", "any": True}, None),
                (
                    "CONFIRM",
                    {"type": "NUMPAD_ENTER", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "PRECISION_ON",
                    {"type": "RIGHT_SHIFT", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "PRECISION_OFF",
                    {"type": "RIGHT_SHIFT", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "PRECISION_ON",
                    {"type": "LEFT_SHIFT", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "PRECISION_OFF",
                    {"type": "LEFT_SHIFT", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "SNAP_ON",
                    {"type": "RIGHT_CTRL", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "SNAP_OFF",
                    {"type": "RIGHT_CTRL", "value": "RELEASE", "any": True},
                    None,
                ),
                ("SNAP_ON", {"type": "LEFT_CTRL", "value": "PRESS", "any": True}, None),
                (
                    "SNAP_OFF",
                    {"type": "LEFT_CTRL", "value": "RELEASE", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Generic Tool: Annotate",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.annotate",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "DRAW"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "DRAW"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Generic Tool: Annotate Eraser",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.annotate",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Generic Tool: Annotate Line",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.annotate",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "DRAW_STRAIGHT"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "EVT_TWEAK_M", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "DRAW_STRAIGHT"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Generic Tool: Annotate Polygon",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.annotate",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "DRAW_POLY"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "MIDDLEMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "DRAW_POLY"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.annotate",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Graph Editor",
        {"space_type": "GRAPH_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                ("wm.search_menu", {"type": "TAB", "value": "PRESS"}, None),
                (
                    "screen.frame_offset",
                    {"type": "X", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "screen.frame_offset",
                    {"type": "C", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("end", True),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("end", False),
                        ],
                    },
                ),
                (
                    "graph.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect_all", True),
                            ("column", False),
                            ("curves", False),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", True),
                            ("curves", False),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("curves", False),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", True),
                            ("curves", False),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", False),
                            ("curves", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("curves", True),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "CHECK"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "LEFT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "RIGHT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "Q", "value": "PRESS"},
                    {
                        "properties": [
                            ("axis_range", False),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "Q", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("tweak", True),
                            ("mode", "SET"),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("tweak", True),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("tweak", True),
                            ("mode", "SUB"),
                        ],
                    },
                ),
                ("graph.select_more", {"type": "UP_ARROW", "value": "PRESS"}, None),
                ("graph.select_less", {"type": "DOWN_ARROW", "value": "PRESS"}, None),
                (
                    "graph.select_linked",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "graph.duplicate_move",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("graph.keyframe_insert", {"type": "S", "value": "PRESS"}, None),
                ("graph.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                ("graph.paste", {"type": "V", "value": "PRESS", "ctrl": True}, None),
                (
                    "graph.paste",
                    {"type": "V", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    },
                ),
                (
                    "graph.previewrange_set",
                    {"type": "P", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "active": False,
                    },
                ),
                ("graph.view_all", {"type": "A", "value": "PRESS"}, None),
                ("graph.view_all", {"type": "NDOF_BUTTON_FIT", "value": "PRESS"}, None),
                ("graph.view_selected", {"type": "F", "value": "PRESS"}, None),
                (
                    "graph.view_frame",
                    {"type": "A", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "anim.channels_editable_toggle",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_M", "value": "ANY"}, None),
                (
                    "transform.transform",
                    {"type": "Y", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_EXTEND"),
                        ],
                    },
                ),
                ("transform.rotate", {"type": "E", "value": "PRESS"}, None),
                ("transform.resize", {"type": "R", "value": "PRESS"}, None),
                (
                    "wm.context_toggle",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_fcurve"),
                        ],
                    },
                ),
                (
                    "wm.context_menu_enum",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.auto_snap"),
                        ],
                    },
                ),
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                ("marker.rename", {"type": "RET", "value": "PRESS"}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "X", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_snap_pie"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Graph Editor Generic",
        {"space_type": "GRAPH_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.call_panel",
                    {"type": "RET", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "TOPBAR_PT_name"),
                            ("keep_open", False),
                        ],
                    },
                ),
                (
                    "anim.channels_find",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "graph.hide",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "graph.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                ("graph.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
            ],
        },
    ),
    (
        "Grease Pencil",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.active_frames_delete_all",
                    {"type": "BACK_SPACE", "value": "PRESS", "key_modifier": "D"},
                    None,
                ),
                (
                    "gpencil.active_frames_delete_all",
                    {"type": "DEL", "value": "PRESS", "key_modifier": "D"},
                    None,
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Edit Mode",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "gpencil.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_linked",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "gpencil.select_alternate",
                    {"type": "L", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                ("gpencil.select_more", {"type": "UP_ARROW", "value": "PRESS"}, None),
                ("gpencil.select_less", {"type": "DOWN_ARROW", "value": "PRESS"}, None),
                (
                    "gpencil.duplicate_move",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_gpencil_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_gpencil_delete"),
                        ],
                    },
                ),
                (
                    "gpencil.dissolve",
                    {"type": "BACK_SPACE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "gpencil.dissolve",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "gpencil.active_frames_delete_all",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.active_frames_delete_all",
                    {"type": "DEL", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_gpencil_edit_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_gpencil_edit_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "P", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GPENCIL_MT_separate"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "gpencil.stroke_join",
                    {"type": "J", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "gpencil.stroke_join",
                    {"type": "J", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", "JOINCOPY"),
                        ],
                    },
                ),
                ("gpencil.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                ("gpencil.paste", {"type": "V", "value": "PRESS", "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": "X", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "GPENCIL_MT_snap"),
                        ],
                    },
                ),
                ("gpencil.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "gpencil.hide",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "gpencil.layer_isolate",
                    {"type": "NUMPAD_ASTERIX", "value": "PRESS"},
                    None,
                ),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "wm.context_toggle",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "GPENCIL_MT_gpencil_vertex_group"),
                        ],
                    },
                ),
                (
                    "gpencil.selectmode_toggle",
                    {"type": "ONE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", 0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "gpencil.selectmode_toggle",
                    {"type": "TWO", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", 1),
                        ],
                        "active": False,
                    },
                ),
                (
                    "gpencil.selectmode_toggle",
                    {"type": "THREE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", 2),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "Q", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_box"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.move"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.rotate"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "R", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.scale"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.transform"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "D", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.annotate"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.measure"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "C", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.cursor"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "U", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "builtin.extrude"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "R", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "builtin.radius"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "builtin.bend"),
                            ("cycle", True),
                        ],
                        "active": False,
                    },
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Paint (Draw brush)",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "DRAW"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "DRAW"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "DRAW_STRAIGHT"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                ("gpencil.draw", {"type": "O", "value": "PRESS"}, None),
                ("gpencil.draw", {"type": "J", "value": "PRESS"}, None),
                ("gpencil.draw", {"type": "J", "value": "PRESS", "alt": True}, None),
                ("gpencil.draw", {"type": "J", "value": "PRESS", "shift": True}, None),
                ("gpencil.draw", {"type": "K", "value": "PRESS"}, None),
                ("gpencil.draw", {"type": "K", "value": "PRESS", "alt": True}, None),
                ("gpencil.draw", {"type": "K", "value": "PRESS", "shift": True}, None),
                ("gpencil.draw", {"type": "L", "value": "PRESS"}, None),
                ("gpencil.draw", {"type": "L", "value": "PRESS", "alt": True}, None),
                ("gpencil.draw", {"type": "L", "value": "PRESS", "ctrl": True}, None),
                ("gpencil.draw", {"type": "B", "value": "PRESS"}, None),
                (
                    "gpencil.draw",
                    {"type": "P", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "ERASER", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Paint (Erase)",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "ERASER", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "ERASER"),
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.select_box",
                    {"type": "B", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Paint (Fill)",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.fill",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("on_back", False),
                        ],
                    },
                ),
                (
                    "gpencil.fill",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("on_back", True),
                        ],
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "DRAW"),
                            ("wait_for_input", False),
                            ("disable_straight", True),
                        ],
                    },
                ),
                (
                    "gpencil.draw",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "DRAW"),
                            ("wait_for_input", False),
                            ("disable_straight", True),
                            ("disable_fill", True),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Paint Mode",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.radial_control",
                    {"type": "U", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_paint.brush.gpencil_settings.pen_strength",
                            ),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "S", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_paint.brush.size",
                            ),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_gpencil_draw_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_gpencil_draw_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GPENCIL_MT_gpencil_draw_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GPENCIL_MT_gpencil_draw_delete"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "D", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin_brush.Draw"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "F", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin_brush.Fill"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin_brush.Erase"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "K", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.cutter"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "C", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.cursor"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin_brush.Draw"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Sculpt Mode",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_linked",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "gpencil.select_alternate",
                    {"type": "L", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                ("gpencil.select_more", {"type": "UP_ARROW", "value": "PRESS"}, None),
                ("gpencil.select_less", {"type": "DOWN_ARROW", "value": "PRESS"}, None),
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "U", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_sculpt_paint.brush.strength",
                            ),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "S", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_sculpt_paint.brush.size",
                            ),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_gpencil_sculpt_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_gpencil_sculpt_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Vertex Mode",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("gpencil.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "gpencil.select_box",
                    {"type": "B", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "gpencil.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "gpencil.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "gpencil.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True},
                    {
                        "properties": [
                            ("entire_strokes", True),
                        ],
                    },
                ),
                (
                    "gpencil.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("entire_strokes", True),
                        ],
                    },
                ),
                ("gpencil.select_linked", {"type": "L", "value": "PRESS"}, None),
                (
                    "gpencil.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "gpencil.select_alternate",
                    {"type": "L", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "gpencil.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.radial_control",
                    {"type": "F", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_vertex_paint.brush.gpencil_settings.pen_strength",
                            ),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "F", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_vertex_paint.brush.size",
                            ),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "Q", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "space_data.overlay.use_gpencil_edit_lines"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "Q", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            (
                                "data_path",
                                "space_data.overlay.use_gpencil_multiedit_line_only",
                            ),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "D", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin_brush.Draw"),
                        ],
                    },
                ),
                (
                    "gpencil.blank_frame_add",
                    {"type": "I", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.active_frames_delete_all",
                    {"type": "X", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.active_frames_delete_all",
                    {"type": "DEL", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "Y", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GPENCIL_MT_layer_active"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "I", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_gpencil_animation"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_gpencil_vertex_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Weight Mode",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "gpencil.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "gpencil.select_linked",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "gpencil.select_alternate",
                    {"type": "L", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "gpencil.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                ("gpencil.select_more", {"type": "UP_ARROW", "value": "PRESS"}, None),
                ("gpencil.select_less", {"type": "DOWN_ARROW", "value": "PRESS"}, None),
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "gpencil.sculpt_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "U", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_weight_paint.brush.strength",
                            ),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "S", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.gpencil_weight_paint.brush.size",
                            ),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Image",
        {"space_type": "IMAGE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                ("image.view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "image.view_all",
                    {"type": "HOME", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("fit_view", True),
                        ],
                    },
                ),
                (
                    "image.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                ("image.view_pan", {"type": "MIDDLEMOUSE", "value": "PRESS"}, None),
                (
                    "image.view_pan",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                ("image.view_pan", {"type": "TRACKPADPAN", "value": "ANY"}, None),
                ("image.view_all", {"type": "NDOF_BUTTON_FIT", "value": "PRESS"}, None),
                ("image.view_ndof", {"type": "NDOF_MOTION", "value": "ANY"}, None),
                (
                    "image.view_zoom_in",
                    {"type": "WHEELINMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "image.view_zoom_out",
                    {"type": "WHEELOUTMOUSE", "value": "PRESS"},
                    None,
                ),
                ("image.view_zoom_in", {"type": "NUMPAD_PLUS", "value": "PRESS"}, None),
                (
                    "image.view_zoom_out",
                    {"type": "NUMPAD_MINUS", "value": "PRESS"},
                    None,
                ),
                (
                    "image.view_zoom",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("image.view_zoom", {"type": "TRACKPADZOOM", "value": "ANY"}, None),
                (
                    "image.view_zoom",
                    {"type": "TRACKPADPAN", "value": "ANY", "ctrl": True},
                    None,
                ),
                (
                    "image.view_zoom_border",
                    {"type": "B", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_1", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.5),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.25),
                        ],
                        "active": False,
                    },
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.125),
                        ],
                        "active": False,
                    },
                ),
                ("image.change_frame", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                ("image.sample", {"type": "RIGHTMOUSE", "value": "PRESS"}, None),
                (
                    "image.curves_point_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("point", "BLACK_POINT"),
                        ],
                    },
                ),
                (
                    "image.curves_point_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("point", "WHITE_POINT"),
                        ],
                    },
                ),
                (
                    "object.mode_set",
                    {"type": "TAB", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "EDIT"),
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 1),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 2),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "FOUR", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 3),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "FIVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 4),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "SIX", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 5),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "SEVEN", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 6),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "EIGHT", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 7),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_int",
                    {"type": "NINE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.image.render_slots.active_index"),
                            ("value", 8),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_pivot_pie"),
                        ],
                    },
                ),
                (
                    "image.render_border",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "image.clear_render_border",
                    {"type": "B", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_mask_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_mask_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Info",
        {"space_type": "INFO", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.call_panel",
                    {"type": "RET", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "TOPBAR_PT_name"),
                            ("keep_open", False),
                        ],
                    },
                ),
                ("wm.search_menu", {"type": "TAB", "value": "PRESS"}, None),
                ("info.select_pick", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "info.select_pick",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "info.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                ("info.select_box", {"type": "Q", "value": "PRESS"}, None),
                ("info.report_replay", {"type": "R", "value": "PRESS"}, None),
                ("info.report_delete", {"type": "BACK_SPACE", "value": "PRESS"}, None),
                ("info.report_delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "info.report_copy",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "INFO_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "INFO_MT_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Lattice",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "lattice.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "lattice.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "lattice.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "lattice.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "lattice.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "lattice.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "object.vertex_parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    {
                        "active": False,
                    },
                ),
                ("lattice.flip", {"type": "F", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_hook"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_lattice_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_lattice_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Markers",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("wm.search_menu", {"type": "TAB", "value": "PRESS"}, None),
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                ("marker.move", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "marker.duplicate",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("marker.select", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "marker.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "marker.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("camera", True),
                        ],
                    },
                ),
                (
                    "marker.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("camera", True),
                        ],
                    },
                ),
                ("marker.select_box", {"type": "Q", "value": "PRESS"}, None),
                (
                    "marker.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "marker.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "marker.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                ("marker.delete", {"type": "BACK_SPACE", "value": "PRESS"}, None),
                ("marker.delete", {"type": "DEL", "value": "PRESS"}, None),
                ("marker.rename", {"type": "RET", "value": "PRESS"}, None),
                ("marker.move", {"type": "W", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "Mask Editing",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("mask.new", {"type": "N", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "MASK_MT_add"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit_mask"),
                        ],
                    },
                ),
                (
                    "mask.add_vertex_slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.add_feather_vertex_slide",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                ("mask.delete", {"type": "X", "value": "PRESS"}, None),
                ("mask.delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "mask.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "mask.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "mask.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    },
                ),
                ("mask.select_box", {"type": "B", "value": "PRESS"}, None),
                ("mask.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "mask.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "mask.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "mask.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.hide_view_clear",
                    {"type": "H", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "mask.hide_view_set",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "mask.hide_view_set",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "clip.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "mask.cyclic_toggle",
                    {"type": "C", "value": "PRESS", "alt": True},
                    None,
                ),
                ("mask.slide_point", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "mask.slide_spline_curvature",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    None,
                ),
                ("mask.handle_type_set", {"type": "V", "value": "PRESS"}, None),
                (
                    "mask.normals_make_consistent",
                    {"type": "N", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "mask.parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "mask.parent_clear",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "active": False,
                    },
                ),
                ("mask.shape_key_insert", {"type": "I", "value": "PRESS"}, None),
                (
                    "mask.shape_key_clear",
                    {"type": "I", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "mask.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "mask.copy_splines",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.paste_splines",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                (
                    "transform.transform",
                    {"type": "S", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "MASK_SHRINKFATTEN"),
                        ],
                    },
                ),
                (
                    "uv.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Mesh",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "mesh.loop_select",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                            ("ring", False),
                        ],
                    },
                ),
                (
                    "mesh.loop_select",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect", False),
                            ("toggle", False),
                            ("ring", False),
                        ],
                    },
                ),
                (
                    "mesh.loop_select",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", True),
                            ("toggle", False),
                            ("ring", False),
                        ],
                    },
                ),
                (
                    "mesh.loop_select",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK", "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                            ("ring", True),
                        ],
                    },
                ),
                (
                    "mesh.loop_select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "DOUBLE_CLICK",
                        "shift": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect", False),
                            ("toggle", False),
                            ("ring", True),
                        ],
                    },
                ),
                (
                    "mesh.loop_select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "DOUBLE_CLICK",
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", True),
                            ("toggle", False),
                            ("ring", True),
                        ],
                    },
                ),
                (
                    "mesh.shortest_path_pick",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("use_fill", False),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                ("mesh.select_more", {"type": "UP_ARROW", "value": "PRESS"}, None),
                ("mesh.select_less", {"type": "DOWN_ARROW", "value": "PRESS"}, None),
                (
                    "mesh.select_linked",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.hide",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "mesh.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                ("mesh.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "mesh.duplicate_move",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_delete"),
                        ],
                    },
                ),
                (
                    "mesh.dissolve_mode",
                    {"type": "BACK_SPACE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mesh.dissolve_mode",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "Q", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_box"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.move"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.rotate"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "R", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.scale"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.transform"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "D", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.annotate"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.measure"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "C", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.cursor"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "builtin.bevel"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "I", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.inset_faces"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "U", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "builtin.extrude_region"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "K", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.knife"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "C", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "builtin.loop_cut"),
                            ("cycle", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "NLA Editor",
        {"space_type": "NLA_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "nla.click_select",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "nla.click_select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "nla.select_leftright",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "CHECK"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "nla.select_leftright",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "CHECK"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "nla.select_leftright",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "LEFT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "nla.select_leftright",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "RIGHT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "nla.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "nla.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "nla.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "nla.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "nla.select_box",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("axis_range", False),
                        ],
                    },
                ),
                (
                    "nla.select_box",
                    {"type": "B", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                        ],
                    },
                ),
                (
                    "nla.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SET"),
                        ],
                    },
                ),
                (
                    "nla.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "nla.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "nla.previewrange_set",
                    {"type": "P", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "active": False,
                    },
                ),
                ("nla.view_all", {"type": "HOME", "value": "PRESS"}, None),
                ("nla.view_all", {"type": "NDOF_BUTTON_FIT", "value": "PRESS"}, None),
                (
                    "nla.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                (
                    "nla.view_frame",
                    {"type": "NUMPAD_0", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "nla.actionclip_add",
                    {"type": "A", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "nla.transition_add",
                    {"type": "T", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "nla.soundclip_add",
                    {"type": "K", "value": "PRESS", "shift": True},
                    None,
                ),
                ("nla.meta_add", {"type": "G", "value": "PRESS", "ctrl": True}, None),
                (
                    "nla.meta_remove",
                    {"type": "G", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "nla.duplicate",
                    {"type": "D", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("linked", False),
                        ],
                    },
                ),
                (
                    "nla.duplicate",
                    {"type": "D", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("linked", True),
                        ],
                    },
                ),
                ("nla.make_single_user", {"type": "U", "value": "PRESS"}, None),
                ("nla.delete", {"type": "X", "value": "PRESS"}, None),
                ("nla.delete", {"type": "DEL", "value": "PRESS"}, None),
                ("nla.split", {"type": "Y", "value": "PRESS"}, None),
                ("nla.mute_toggle", {"type": "H", "value": "PRESS"}, None),
                ("nla.swap", {"type": "F", "value": "PRESS", "alt": True}, None),
                ("nla.move_up", {"type": "PAGE_UP", "value": "PRESS"}, None),
                ("nla.move_down", {"type": "PAGE_DOWN", "value": "PRESS"}, None),
                (
                    "nla.apply_scale",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("nla.clear_scale", {"type": "S", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "NLA_MT_snap_pie"),
                        ],
                    },
                ),
                (
                    "nla.fmodifier_add",
                    {"type": "M", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "transform.transform",
                    {"type": "G", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TRANSLATION"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "TRANSLATION"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_EXTEND"),
                        ],
                    },
                ),
                (
                    "transform.transform",
                    {"type": "R", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_SCALE"),
                        ],
                    },
                ),
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                ("marker.rename", {"type": "M", "value": "PRESS", "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "NLA_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "NLA_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "anim.change_frame",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Node Editor",
        {"space_type": "NODE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "node.select",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "node.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "node.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "node.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "node.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "node.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "node.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "node.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "node.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "node.select_lasso",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "node.select_lasso",
                    {
                        "type": "EVT_TWEAK_L",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                ("node.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "node.link",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("detach", False),
                        ],
                    },
                ),
                (
                    "node.link",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("detach", True),
                        ],
                    },
                ),
                ("node.resize", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "node.add_reroute",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "shift": True},
                    None,
                ),
                (
                    "node.links_cut",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True},
                    None,
                ),
                (
                    "node.select_link_viewer",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                (
                    "node.backimage_move",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "node.backimage_zoom",
                    {"type": "V", "value": "PRESS"},
                    {
                        "properties": [
                            ("factor", 0.8333333),
                        ],
                    },
                ),
                (
                    "node.backimage_zoom",
                    {"type": "V", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("factor", 1.2),
                        ],
                    },
                ),
                (
                    "node.backimage_fit",
                    {"type": "HOME", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "node.backimage_sample",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "node.link_make",
                    {"type": "F", "value": "PRESS"},
                    {
                        "properties": [
                            ("replace", False),
                        ],
                    },
                ),
                (
                    "node.link_make",
                    {"type": "F", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("replace", True),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "NODE_MT_add"),
                        ],
                    },
                ),
                (
                    "node.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "node.duplicate_move_keep_inputs",
                    {"type": "D", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "node.parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "node.detach",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "active": False,
                    },
                ),
                ("node.join", {"type": "J", "value": "PRESS", "ctrl": True}, None),
                ("node.hide_toggle", {"type": "H", "value": "PRESS"}, None),
                ("node.mute_toggle", {"type": "M", "value": "PRESS"}, None),
                (
                    "node.preview_toggle",
                    {"type": "H", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "node.hide_socket_toggle",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("node.view_all", {"type": "HOME", "value": "PRESS"}, None),
                ("node.view_all", {"type": "NDOF_BUTTON_FIT", "value": "PRESS"}, None),
                (
                    "node.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                (
                    "node.select_box",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("tweak", False),
                        ],
                    },
                ),
                ("node.delete", {"type": "X", "value": "PRESS"}, None),
                ("node.delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "node.delete_reconnect",
                    {"type": "X", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "node.delete_reconnect",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "node.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "node.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "node.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "node.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "node.select_linked_to",
                    {"type": "L", "value": "PRESS", "shift": True},
                    None,
                ),
                ("node.select_linked_from", {"type": "L", "value": "PRESS"}, None),
                (
                    "node.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "node.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "node.select_same_type_step",
                    {"type": "RIGHT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("prev", False),
                        ],
                    },
                ),
                (
                    "node.select_same_type_step",
                    {"type": "LEFT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("prev", True),
                        ],
                    },
                ),
                ("node.find_node", {"type": "F", "value": "PRESS", "ctrl": True}, None),
                (
                    "node.group_make",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "node.group_ungroup",
                    {"type": "G", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "node.group_separate",
                    {"type": "P", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "node.group_edit",
                    {"type": "TAB", "value": "PRESS"},
                    {
                        "properties": [
                            ("exit", False),
                        ],
                    },
                ),
                (
                    "node.group_edit",
                    {"type": "TAB", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("exit", True),
                        ],
                    },
                ),
                (
                    "node.read_viewlayers",
                    {"type": "R", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("node.render_changed", {"type": "Z", "value": "PRESS"}, None),
                (
                    "node.clipboard_copy",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "node.clipboard_paste",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "node.viewer_border",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "node.clear_viewer_border",
                    {"type": "B", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("node.translate_attach", {"type": "G", "value": "PRESS"}, None),
                (
                    "node.translate_attach",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
                (
                    "node.translate_attach",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                (
                    "node.move_detach_links",
                    {"type": "D", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "node.move_detach_links_release",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "alt": True},
                    None,
                ),
                (
                    "node.move_detach_links",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "alt": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_snap"),
                        ],
                    },
                ),
                (
                    "wm.context_menu_enum",
                    {"type": "TAB", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.snap_node_element"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "NODE_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "NODE_MT_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Object Mode",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "screen.frame_offset",
                    {"type": "X", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "screen.frame_offset",
                    {"type": "C", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("end", True),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("end", False),
                        ],
                    },
                ),
                (
                    "object.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "object.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "object.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                ("object.select_more", {"type": "UP_ARROW", "value": "PRESS"}, None),
                ("object.select_less", {"type": "DOWN_ARROW", "value": "PRESS"}, None),
                (
                    "object.select_linked",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "object.select_hierarchy",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "PARENT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "object.select_hierarchy",
                    {"type": "LEFT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "PARENT"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "object.select_hierarchy",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "CHILD"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "object.select_hierarchy",
                    {"type": "RIGHT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "CHILD"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "object.parent_set",
                    {"type": "P", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path",
                                "tool_settings.use_proportional_edit_objects",
                            ),
                        ],
                    },
                ),
                (
                    "object.parent_clear",
                    {"type": "P", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "object.location_clear",
                    {"type": "W", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("clear_delta", False),
                        ],
                    },
                ),
                (
                    "object.rotation_clear",
                    {"type": "E", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("clear_delta", False),
                        ],
                    },
                ),
                (
                    "object.scale_clear",
                    {"type": "R", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("clear_delta", False),
                        ],
                    },
                ),
                (
                    "object.delete",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_global", False),
                            ("confirm", False),
                        ],
                    },
                ),
                (
                    "object.delete",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_global", True),
                            ("confirm", False),
                        ],
                    },
                ),
                (
                    "object.delete",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_global", False),
                            ("confirm", False),
                        ],
                    },
                ),
                (
                    "object.delete",
                    {"type": "DEL", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_global", True),
                            ("confirm", False),
                        ],
                    },
                ),
                (
                    "object.duplicate_move",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "anim.keyframe_insert_menu",
                    {"type": "S", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "anim.keyframe_insert_by_name",
                    {"type": "S", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LocRotScale"),
                        ],
                    },
                ),
                (
                    "anim.keyframe_insert_by_name",
                    {"type": "W", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "Location"),
                        ],
                    },
                ),
                (
                    "anim.keyframe_insert_by_name",
                    {"type": "E", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "Rotation"),
                        ],
                    },
                ),
                (
                    "anim.keyframe_insert_by_name",
                    {"type": "R", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "Scaling"),
                        ],
                    },
                ),
                (
                    "anim.keyframe_delete_v3d",
                    {"type": "S", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "anim.keying_set_active_set",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_object_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_object_context_menu"),
                        ],
                    },
                ),
                (
                    "object.move_to_collection",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "object.link_to_collection",
                    {"type": "G", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "object.hide_view_clear",
                    {"type": "H", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "object.hide_view_set",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "object.hide_view_set",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "Q", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_box"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.move"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.rotate"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "R", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.scale"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.transform"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "D", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.annotate"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.measure"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "C", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.cursor"),
                            ("cycle", True),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "TAB", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_add"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Object Non-modal",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                # Vertices Selection
                (
                    "object.mode_set_with_submode",
                    {"type": "ONE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "EDIT"),
                            ("mesh_select_mode", {"VERT"}),
                        ],
                    },
                ),
                # Edge Selection
                (
                    "object.mode_set_with_submode",
                    {"type": "TWO", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "EDIT"),
                            ("mesh_select_mode", {"EDGE"}),
                        ],
                    },
                ),
                # Face Selection
                (
                    "object.mode_set_with_submode",
                    {"type": "THREE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "EDIT"),
                            ("mesh_select_mode", {"FACE"}),
                        ],
                    },
                ),
                # Escape back to Object mode
                (
                    "object.mode_set",
                    {"type": "Q", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "OBJECT"),
                        ],
                    },
                ),
                # Armature edit mode
                (
                    "object.mode_set",
                    {"type": "ONE", "value": "PRESS", "alt": True, "repeat": True},
                    {
                        "properties": [
                            ("mode", "EDIT"),
                        ],
                    },
                ),
                # Sculpt mode
                (
                    "object.mode_set",
                    {"type": "FOUR", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "SCULPT"),
                        ],
                    },
                ),
                # GreasePencil draw mode
                (
                    "object.mode_set",
                    {"type": "FIVE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "PAINT_GPENCIL"),
                        ],
                    },
                ),
                # GreasePencil sculpt mode
                (
                    "object.mode_set",
                    {"type": "SIX", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "SCULPT_GPENCIL"),
                        ],
                    },
                ),
                # Armature pose mode
                (
                    "object.mode_set",
                    {"type": "FOUR", "value": "PRESS", "alt": True, "repeat": True},
                    {
                        "properties": [
                            ("mode", "POSE"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Outliner",
        {"space_type": "OUTLINER", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "outliner.item_rename",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                ("outliner.item_rename", {"type": "RET", "value": "PRESS"}, None),
                ("wm.search_menu", {"type": "TAB", "value": "PRESS"}, None),
                (
                    "outliner.highlight_update",
                    {"type": "MOUSEMOVE", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "outliner.item_activate",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("extend_range", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("extend_range", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "outliner.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "outliner.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "UP_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "UP"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "UP_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "UP"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "DOWN_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "DOWN"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "DOWN_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "DOWN"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "LEFT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "LEFT"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "LEFT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "LEFT"),
                            ("toggle_all", True),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "RIGHT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "RIGHT"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "RIGHT"),
                            ("toggle_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_openclose",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                (
                    "outliner.item_openclose",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_openclose",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                ("outliner.operation", {"type": "RIGHTMOUSE", "value": "PRESS"}, None),
                (
                    "outliner.item_drag_drop",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
                (
                    "outliner.item_drag_drop",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    None,
                ),
                ("outliner.show_hierarchy", {"type": "A", "value": "PRESS"}, None),
                ("outliner.show_active", {"type": "PERIOD", "value": "PRESS"}, None),
                ("outliner.show_active", {"type": "F", "value": "PRESS"}, None),
                (
                    "outliner.scroll_page",
                    {"type": "PAGE_DOWN", "value": "PRESS"},
                    {
                        "properties": [
                            ("up", False),
                        ],
                    },
                ),
                (
                    "outliner.scroll_page",
                    {"type": "PAGE_UP", "value": "PRESS"},
                    {
                        "properties": [
                            ("up", True),
                        ],
                    },
                ),
                (
                    "outliner.show_one_level",
                    {"type": "NUMPAD_PLUS", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.show_one_level",
                    {"type": "NUMPAD_MINUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("open", False),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "outliner.keyingset_add_selected",
                    {"type": "K", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.keyingset_remove_selected",
                    {"type": "K", "value": "PRESS", "alt": True},
                    None,
                ),
                ("anim.keyframe_insert", {"type": "S", "value": "PRESS"}, None),
                (
                    "anim.keyframe_delete",
                    {"type": "S", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "outliner.drivers_add_selected",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "outliner.drivers_delete_selected",
                    {"type": "D", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "outliner.collection_delete",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    None,
                ),
                ("outliner.collection_delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "outliner.object_operation",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    None,
                ),
                ("outliner.object_operation", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "object.move_to_collection",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "object.link_to_collection",
                    {"type": "M", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "outliner.collection_exclude_set",
                    {"type": "E", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.collection_exclude_clear",
                    {"type": "E", "value": "PRESS", "alt": True},
                    None,
                ),
                ("outliner.hide", {"type": "H", "value": "PRESS", "ctrl": True}, None),
                (
                    "outliner.unhide_all",
                    {"type": "H", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "outliner.id_copy",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "outliner.id_paste",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Paint Curve",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "paintcurve.add_point_slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "paintcurve.select",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "paintcurve.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "paintcurve.slide",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("align", False),
                        ],
                    },
                ),
                (
                    "paintcurve.slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("align", True),
                        ],
                    },
                ),
                (
                    "paintcurve.select",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                ("paintcurve.cursor", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "paintcurve.delete_point",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    None,
                ),
                ("paintcurve.delete_point", {"type": "DEL", "value": "PRESS"}, None),
                ("paintcurve.draw", {"type": "RET", "value": "PRESS"}, None),
                ("paintcurve.draw", {"type": "NUMPAD_ENTER", "value": "PRESS"}, None),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.rotate", {"type": "E", "value": "PRESS"}, None),
                ("transform.resize", {"type": "R", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "Paint Stroke Modal",
        {"space_type": "EMPTY", "region_type": "WINDOW", "modal": True},
        {
            "items": [
                ("CANCEL", {"type": "ESC", "value": "PRESS", "any": True}, None),
            ],
        },
    ),
    (
        "Paint Vertex Selection (Weight, Vertex)",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "paint.vert_select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "paint.vert_select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "paint.vert_select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "paint.vert_select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "view3d.select_box",
                    {"type": "B", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "view3d.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                ("view3d.select_circle", {"type": "C", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "Particle",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "particle.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "particle.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "particle.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "particle.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "particle.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "particle.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "particle.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "particle.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    },
                ),
                (
                    "particle.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("particle.delete", {"type": "X", "value": "PRESS"}, None),
                ("particle.delete", {"type": "DEL", "value": "PRESS"}, None),
                ("particle.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "particle.hide",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "particle.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                ("particle.brush_edit", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "particle.brush_edit",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.radial_control",
                    {"type": "F", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.particle_edit.brush.size",
                            ),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "F", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.particle_edit.brush.strength",
                            ),
                        ],
                    },
                ),
                (
                    "particle.weight_set",
                    {"type": "K", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.context_set_enum",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.particle_edit.select_mode"),
                            ("value", "PATH"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.particle_edit.select_mode"),
                            ("value", "POINT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.particle_edit.select_mode"),
                            ("value", "TIP"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_particle_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_particle_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Pose",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "object.parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_add"),
                        ],
                    },
                ),
                (
                    "pose.hide",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "pose.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                ("pose.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_pose_apply"),
                        ],
                    },
                ),
                ("pose.rot_clear", {"type": "R", "value": "PRESS", "alt": True}, None),
                ("pose.loc_clear", {"type": "G", "value": "PRESS", "alt": True}, None),
                (
                    "pose.scale_clear",
                    {"type": "S", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "pose.quaternions_flip",
                    {"type": "F", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "pose.rotation_mode_set",
                    {"type": "R", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("pose.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                (
                    "pose.paste",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("flipped", False),
                        ],
                    },
                ),
                (
                    "pose.paste",
                    {"type": "V", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    },
                ),
                (
                    "pose.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "pose.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "pose.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "pose.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "pose.select_parent",
                    {"type": "P", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "pose.select_hierarchy",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "PARENT"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "pose.select_hierarchy",
                    {"type": "LEFT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "PARENT"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "pose.select_hierarchy",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("direction", "CHILD"),
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "pose.select_hierarchy",
                    {"type": "RIGHT_BRACKET", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("direction", "CHILD"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "pose.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("pose.select_linked_pick", {"type": "L", "value": "PRESS"}, None),
                (
                    "pose.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "pose.select_mirror",
                    {"type": "M", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "pose.constraint_add_with_targets",
                    {"type": "C", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "pose.constraints_clear",
                    {"type": "C", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("pose.ik_add", {"type": "I", "value": "PRESS", "shift": True}, None),
                (
                    "pose.ik_clear",
                    {"type": "I", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_pose_group"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_bone_options_toggle"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_bone_options_enable"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_bone_options_disable"),
                        ],
                    },
                ),
                (
                    "armature.layers_show_all",
                    {"type": "ACCENT_GRAVE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "armature.armature_layers",
                    {"type": "M", "value": "PRESS", "shift": True},
                    None,
                ),
                ("pose.bone_layers", {"type": "M", "value": "PRESS"}, None),
                (
                    "transform.bbone_resize",
                    {"type": "S", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("anim.keyframe_insert_menu", {"type": "I", "value": "PRESS"}, None),
                (
                    "anim.keyframe_delete_v3d",
                    {"type": "I", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "anim.keying_set_active_set",
                    {
                        "type": "I",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "poselib.browse_interactive",
                    {"type": "L", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "poselib.pose_add",
                    {"type": "L", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "poselib.pose_remove",
                    {"type": "L", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                (
                    "poselib.pose_rename",
                    {"type": "L", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                ("pose.push", {"type": "T", "value": "PRESS", "ctrl": True}, None),
                ("pose.relax", {"type": "T", "value": "PRESS", "alt": True}, None),
                (
                    "pose.breakdown",
                    {"type": "T", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_pose_propagate"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "ONE", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 1),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "TWO", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 2),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "THREE", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 3),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "FOUR", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 4),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "FIVE", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 5),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "SIX", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 6),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "SEVEN", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 7),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "EIGHT", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 8),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "NINE", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 9),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.hide_collection",
                    {"type": "ZERO", "value": "PRESS", "any": True},
                    {
                        "properties": [
                            ("collection_index", 10),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_pose_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_pose_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Property Editor",
        {"space_type": "PROPERTIES", "region_type": "WINDOW"},
        {
            "items": [
                ("wm.search_menu", {"type": "TAB", "value": "PRESS"}, None),
                (
                    "buttons.context_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("direction", "PREV"),
                        ],
                    },
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("direction", "NEXT"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Region Context Menu",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "screen.region_context_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    None,
                ),
            ],
        },
    ),
    (
        "Screen",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("screen.repeat_last", {"type": "G", "value": "PRESS"}, None),
                (
                    "screen.userpref_show",
                    {"type": "COMMA", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "screen.animation_step",
                    {"type": "TIMER0", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "screen.region_blend",
                    {"type": "TIMERREGION", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "TAB", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("direction", "NEXT"),
                        ],
                    },
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "TAB", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", "PREV"),
                        ],
                    },
                ),
                (
                    "screen.workspace_cycle",
                    {"type": "PAGE_DOWN", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("direction", "NEXT"),
                        ],
                    },
                ),
                (
                    "screen.workspace_cycle",
                    {"type": "PAGE_UP", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("direction", "PREV"),
                        ],
                    },
                ),
                ("file.execute", {"type": "RET", "value": "PRESS"}, None),
                ("file.execute", {"type": "NUMPAD_ENTER", "value": "PRESS"}, None),
                ("file.cancel", {"type": "ESC", "value": "PRESS"}, None),
                ("ed.undo", {"type": "Z", "value": "PRESS"}, None),
                ("ed.redo", {"type": "Z", "value": "PRESS", "shift": True}, None),
                (
                    "ed.undo_history",
                    {"type": "Z", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("render.view_cancel", {"type": "ESC", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "Screen Editing",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "screen.actionzone",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("modifier", 0),
                        ],
                    },
                ),
                (
                    "screen.actionzone",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("modifier", 1),
                        ],
                    },
                ),
                (
                    "screen.actionzone",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("modifier", 2),
                        ],
                    },
                ),
                (
                    "screen.area_split",
                    {"type": "ACTIONZONE_AREA", "value": "ANY"},
                    None,
                ),
                ("screen.area_join", {"type": "ACTIONZONE_AREA", "value": "ANY"}, None),
                (
                    "screen.area_dupli",
                    {"type": "ACTIONZONE_AREA", "value": "ANY", "shift": True},
                    None,
                ),
                (
                    "screen.area_swap",
                    {"type": "ACTIONZONE_AREA", "value": "ANY", "ctrl": True},
                    None,
                ),
                (
                    "screen.region_scale",
                    {"type": "ACTIONZONE_REGION", "value": "ANY"},
                    None,
                ),
                (
                    "screen.screen_full_area",
                    {"type": "ACTIONZONE_FULLSCREEN", "value": "ANY"},
                    {
                        "properties": [
                            ("use_hide_panels", True),
                        ],
                    },
                ),
                ("screen.area_move", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                ("screen.area_options", {"type": "RIGHTMOUSE", "value": "PRESS"}, None),
                (
                    "render.render",
                    {"type": "RET", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_viewport", True),
                        ],
                    },
                ),
                (
                    "render.render",
                    {"type": "RET", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("animation", True),
                            ("use_viewport", True),
                        ],
                    },
                ),
                ("render.view_cancel", {"type": "ESC", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "Sculpt",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "sculpt.brush_stroke",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "NORMAL"),
                        ],
                    },
                ),
                (
                    "sculpt.brush_stroke",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "INVERT"),
                        ],
                    },
                ),
                (
                    "sculpt.brush_stroke",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "SMOOTH"),
                        ],
                    },
                ),
                (
                    "paint.hide_show",
                    {"type": "H", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "SHOW"),
                            ("area", "INSIDE"),
                        ],
                    },
                ),
                (
                    "paint.hide_show",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "HIDE"),
                            ("area", "INSIDE"),
                        ],
                    },
                ),
                (
                    "paint.hide_show",
                    {"type": "H", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("action", "SHOW"),
                            ("area", "ALL"),
                        ],
                    },
                ),
                (
                    "object.subdivision_set",
                    {
                        "type": "ACCENT_GRAVE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("level", 0),
                            ("relative", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.subdivision_set",
                    {
                        "type": "ONE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("level", 1),
                            ("relative", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.subdivision_set",
                    {
                        "type": "TWO",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("level", 2),
                            ("relative", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.subdivision_set",
                    {
                        "type": "THREE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("level", 3),
                            ("relative", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.subdivision_set",
                    {
                        "type": "FOUR",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("level", 4),
                            ("relative", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.subdivision_set",
                    {
                        "type": "FIVE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("level", 5),
                            ("relative", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.subdivision_set",
                    {"type": "PAGE_UP", "value": "PRESS"},
                    {
                        "properties": [
                            ("level", 1),
                            ("relative", True),
                        ],
                        "active": False,
                    },
                ),
                (
                    "object.subdivision_set",
                    {"type": "PAGE_DOWN", "value": "PRESS"},
                    {
                        "properties": [
                            ("level", -1),
                            ("relative", True),
                        ],
                        "active": False,
                    },
                ),
                (
                    "paint.mask_flood_fill",
                    {"type": "A", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "VALUE"),
                            ("value", 0.0),
                        ],
                    },
                ),
                (
                    "paint.mask_flood_fill",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("mode", "VALUE"),
                            ("value", 1.0),
                        ],
                    },
                ),
                (
                    "paint.mask_flood_fill",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "INVERT"),
                        ],
                    },
                ),
                (
                    "paint.mask_lasso_gesture",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "scene.tool_settings.sculpt.show_mask"),
                        ],
                    },
                ),
                (
                    "sculpt.mask_filter",
                    {
                        "type": "A",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("filter_type", "SMOOTH"),
                            ("auto_iteration_count", True),
                        ],
                    },
                ),
                (
                    "sculpt.dynamic_topology_toggle",
                    {"type": "FIVE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "sculpt.set_detail_size",
                    {"type": "D", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "object.voxel_remesh",
                    {"type": "Y", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "object.quadriflow_remesh",
                    {"type": "Y", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "brush.scale_size",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("scalar", 0.9),
                        ],
                    },
                ),
                (
                    "brush.scale_size",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("scalar", 1.1111112),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "S", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path_primary", "tool_settings.sculpt.brush.size"),
                            (
                                "data_path_secondary",
                                "tool_settings.unified_paint_settings.size",
                            ),
                            (
                                "use_secondary",
                                "tool_settings.unified_paint_settings.use_unified_size",
                            ),
                            (
                                "rotation_path",
                                "tool_settings.sculpt.brush.texture_slot.angle",
                            ),
                            (
                                "color_path",
                                "tool_settings.sculpt.brush.cursor_color_add",
                            ),
                            ("fill_color_path", ""),
                            ("fill_color_override_path", ""),
                            ("fill_color_override_test_path", ""),
                            ("zoom_path", ""),
                            ("image_id", "tool_settings.sculpt.brush"),
                            ("secondary_tex", False),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "U", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.sculpt.brush.strength",
                            ),
                            (
                                "data_path_secondary",
                                "tool_settings.unified_paint_settings.strength",
                            ),
                            (
                                "use_secondary",
                                "tool_settings.unified_paint_settings.use_unified_strength",
                            ),
                            (
                                "rotation_path",
                                "tool_settings.sculpt.brush.texture_slot.angle",
                            ),
                            (
                                "color_path",
                                "tool_settings.sculpt.brush.cursor_color_add",
                            ),
                            ("fill_color_path", ""),
                            ("fill_color_override_path", ""),
                            ("fill_color_override_test_path", ""),
                            ("zoom_path", ""),
                            ("image_id", "tool_settings.sculpt.brush"),
                            ("secondary_tex", False),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.sculpt.brush.texture_slot.angle",
                            ),
                            ("data_path_secondary", ""),
                            ("use_secondary", ""),
                            (
                                "rotation_path",
                                "tool_settings.sculpt.brush.texture_slot.angle",
                            ),
                            (
                                "color_path",
                                "tool_settings.sculpt.brush.cursor_color_add",
                            ),
                            ("fill_color_path", ""),
                            ("fill_color_override_path", ""),
                            ("fill_color_override_test_path", ""),
                            ("zoom_path", ""),
                            ("image_id", "tool_settings.sculpt.brush"),
                            ("secondary_tex", False),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TRANSLATION"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "SCALE"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ROTATION"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "TRANSLATION"),
                            ("texmode", "SECONDARY"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {
                        "type": "RIGHTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SCALE"),
                            ("texmode", "SECONDARY"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ROTATION"),
                            ("texmode", "SECONDARY"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "S", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "SMOOTH"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "THREE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("sculpt_tool", "PINCH"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "FOUR", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("sculpt_tool", "INFLATE"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "GRAB"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "LAYER"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "FIVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "FLATTEN"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "TWO", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("sculpt_tool", "CLAY"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "MASK"),
                            ("toggle", True),
                            ("create_missing", True),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "R", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "ROTATE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "TWO", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("sculpt_tool", "NUDGE"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "THUMB"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "FOUR", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("sculpt_tool", "SNAKE_HOOK"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "BLOB"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "ONE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("sculpt_tool", "DRAW"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_sculpt_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_sculpt_context_menu"),
                        ],
                    },
                ),
                (
                    "object.voxel_size_edit",
                    {"type": "Y", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "paint.brush_select",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "CLAY_STRIPS"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "DRAW_SHARP"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "FOUR", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "FILL"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "G", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "DRAW_FACE_SETS"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("sculpt_tool", "POSE"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "FIVE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("sculpt_tool", "CLOTH"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.transform"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "P", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.mesh_filter"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "ONE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("sculpt_tool", "ELASTIC_DEFORM"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Sequencer",
        {"space_type": "SEQUENCE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.split",
                    {"type": "K", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "SOFT"),
                        ],
                    },
                ),
                (
                    "sequencer.split",
                    {"type": "K", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "HARD"),
                        ],
                    },
                ),
                (
                    "sequencer.mute",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "sequencer.mute",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "sequencer.unmute",
                    {"type": "H", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "sequencer.unmute",
                    {"type": "H", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "sequencer.lock",
                    {"type": "L", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "sequencer.unlock",
                    {"type": "L", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                ("sequencer.reassign_inputs", {"type": "R", "value": "PRESS"}, None),
                (
                    "sequencer.reload",
                    {"type": "R", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "sequencer.reload",
                    {"type": "R", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("adjust_length", True),
                        ],
                    },
                ),
                (
                    "sequencer.refresh_all",
                    {"type": "R", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.offset_clear",
                    {"type": "O", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "sequencer.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                ("sequencer.delete", {"type": "X", "value": "PRESS"}, None),
                ("sequencer.delete", {"type": "DEL", "value": "PRESS"}, None),
                ("sequencer.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                (
                    "sequencer.paste",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("sequencer.images_separate", {"type": "Y", "value": "PRESS"}, None),
                ("sequencer.meta_toggle", {"type": "TAB", "value": "PRESS"}, None),
                (
                    "sequencer.meta_make",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.meta_separate",
                    {"type": "G", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("sequencer.view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "sequencer.view_all",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
                (
                    "sequencer.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                (
                    "sequencer.view_frame",
                    {"type": "NUMPAD_0", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "sequencer.strip_jump",
                    {"type": "PAGE_UP", "value": "PRESS"},
                    {
                        "properties": [
                            ("next", True),
                            ("center", False),
                        ],
                    },
                ),
                (
                    "sequencer.strip_jump",
                    {"type": "PAGE_DOWN", "value": "PRESS"},
                    {
                        "properties": [
                            ("next", False),
                            ("center", False),
                        ],
                    },
                ),
                (
                    "sequencer.strip_jump",
                    {"type": "PAGE_UP", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("next", True),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.strip_jump",
                    {"type": "PAGE_DOWN", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("next", False),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.swap",
                    {"type": "LEFT_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("side", "LEFT"),
                        ],
                    },
                ),
                (
                    "sequencer.swap",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("side", "RIGHT"),
                        ],
                    },
                ),
                (
                    "sequencer.gap_remove",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                (
                    "sequencer.gap_remove",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("all", True),
                        ],
                    },
                ),
                (
                    "sequencer.gap_insert",
                    {"type": "EQUAL", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "sequencer.snap",
                    {"type": "S", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "sequencer.swap_inputs",
                    {"type": "S", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 1),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 2),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 3),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "FOUR", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 4),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "FIVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 5),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "SIX", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 6),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "SEVEN", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 7),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "EIGHT", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 8),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "NINE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 9),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "ZERO", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 10),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("linked_handle", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_handle", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("linked_time", True),
                            ("side_of_frame", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_time", True),
                            ("side_of_frame", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "sequencer.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "SET"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                            ("tweak", True),
                        ],
                    },
                ),
                ("sequencer.select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "sequencer.select_box",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("include_handles", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_add"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "C", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_change"),
                        ],
                    },
                ),
                ("sequencer.slip", {"type": "S", "value": "PRESS"}, None),
                (
                    "wm.context_set_int",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "scene.sequence_editor.overlay_frame"),
                            ("value", 0),
                        ],
                    },
                ),
                ("transform.seq_slide", {"type": "G", "value": "PRESS"}, None),
                ("transform.seq_slide", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "transform.transform",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_EXTEND"),
                        ],
                    },
                ),
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                ("marker.rename", {"type": "M", "value": "PRESS", "ctrl": True}, None),
                (
                    "sequencer.select_side_of_frame",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("side", "LEFT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_side_of_frame",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("side", "RIGHT"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "SequencerPreview",
        {"space_type": "SEQUENCE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "sequencer.view_all_preview",
                    {"type": "HOME", "value": "PRESS"},
                    None,
                ),
                (
                    "sequencer.view_all_preview",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
                ("sequencer.view_ghost_border", {"type": "O", "value": "PRESS"}, None),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_1", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.5),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.25),
                        ],
                        "active": False,
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.125),
                        ],
                        "active": False,
                    },
                ),
                ("sequencer.sample", {"type": "RIGHTMOUSE", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "Standard Modal Map",
        {"space_type": "EMPTY", "region_type": "WINDOW", "modal": True},
        {
            "items": [
                ("CANCEL", {"type": "ESC", "value": "PRESS", "any": True}, None),
                ("APPLY", {"type": "LEFTMOUSE", "value": "ANY", "any": True}, None),
                ("APPLY", {"type": "RET", "value": "PRESS", "any": True}, None),
                (
                    "APPLY",
                    {"type": "NUMPAD_ENTER", "value": "PRESS", "any": True},
                    None,
                ),
                ("SNAP", {"type": "LEFT_CTRL", "value": "PRESS", "any": True}, None),
                (
                    "SNAP_OFF",
                    {"type": "LEFT_CTRL", "value": "RELEASE", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Text",
        {"space_type": "TEXT_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_cycle_int",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", False),
                        ],
                    },
                ),
                (
                    "wm.context_cycle_int",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", True),
                        ],
                    },
                ),
                (
                    "wm.context_cycle_int",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", False),
                        ],
                    },
                ),
                (
                    "wm.context_cycle_int",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.font_size"),
                            ("reverse", True),
                        ],
                    },
                ),
                ("text.new", {"type": "N", "value": "PRESS", "alt": True}, None),
                ("text.open", {"type": "O", "value": "PRESS", "alt": True}, None),
                ("text.reload", {"type": "R", "value": "PRESS", "alt": True}, None),
                ("text.save", {"type": "S", "value": "PRESS", "alt": True}, None),
                (
                    "text.save_as",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "text.run_script",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "active": False,
                    },
                ),
                ("text.cut", {"type": "X", "value": "PRESS", "ctrl": True}, None),
                ("text.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                ("text.paste", {"type": "V", "value": "PRESS", "ctrl": True}, None),
                ("text.cut", {"type": "DEL", "value": "PRESS", "shift": True}, None),
                ("text.copy", {"type": "INSERT", "value": "PRESS", "ctrl": True}, None),
                (
                    "text.paste",
                    {"type": "INSERT", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "text.duplicate_line",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "text.select_all",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "text.select_line",
                    {"type": "A", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "text.select_word",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                (
                    "text.move_lines",
                    {"type": "UP_ARROW", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", "UP"),
                        ],
                    },
                ),
                (
                    "text.move_lines",
                    {
                        "type": "DOWN_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("direction", "DOWN"),
                        ],
                    },
                ),
                (
                    "text.indent_or_autocomplete",
                    {"type": "TAB", "value": "PRESS"},
                    None,
                ),
                (
                    "text.unindent",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "text.comment_toggle",
                    {"type": "SLASH", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "text.move",
                    {"type": "HOME", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LINE_BEGIN"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "END", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LINE_END"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "E", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "LINE_END"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "E", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", "LINE_END"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "LEFT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "RIGHT_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_CHARACTER"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "LEFT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "UP_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_LINE"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "DOWN_ARROW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_LINE"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "PAGE_UP", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_PAGE"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "PAGE_DOWN", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_PAGE"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "HOME", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "FILE_TOP"),
                        ],
                    },
                ),
                (
                    "text.move",
                    {"type": "END", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "FILE_BOTTOM"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "HOME", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "LINE_BEGIN"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "END", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "LINE_END"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "LEFT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "NEXT_CHARACTER"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "UP_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_LINE"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "DOWN_ARROW", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "NEXT_LINE"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "PAGE_UP", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_PAGE"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "PAGE_DOWN", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "NEXT_PAGE"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "HOME", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", "FILE_TOP"),
                        ],
                    },
                ),
                (
                    "text.move_select",
                    {"type": "END", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", "FILE_BOTTOM"),
                        ],
                    },
                ),
                (
                    "text.delete",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "NEXT_CHARACTER"),
                        ],
                    },
                ),
                (
                    "text.delete",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "text.delete",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_CHARACTER"),
                        ],
                    },
                ),
                (
                    "text.delete",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "NEXT_WORD"),
                        ],
                    },
                ),
                (
                    "text.delete",
                    {"type": "BACK_SPACE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "PREVIOUS_WORD"),
                        ],
                    },
                ),
                ("text.overwrite_toggle", {"type": "INSERT", "value": "PRESS"}, None),
                ("text.scroll_bar", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                ("text.scroll_bar", {"type": "MIDDLEMOUSE", "value": "PRESS"}, None),
                ("text.scroll", {"type": "MIDDLEMOUSE", "value": "PRESS"}, None),
                ("text.scroll", {"type": "TRACKPADPAN", "value": "ANY"}, None),
                ("text.selection_set", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("text.cursor_set", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "text.selection_set",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "text.scroll",
                    {"type": "WHEELUPMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("lines", -1),
                        ],
                    },
                ),
                (
                    "text.scroll",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("lines", 1),
                        ],
                    },
                ),
                ("text.line_break", {"type": "RET", "value": "PRESS"}, None),
                ("text.line_break", {"type": "NUMPAD_ENTER", "value": "PRESS"}, None),
                (
                    "text.line_number",
                    {"type": "TEXTINPUT", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "TEXT_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "text.insert",
                    {"type": "TEXTINPUT", "value": "ANY", "any": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Time Scrub",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("anim.change_frame", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                ("graph.cursor_set", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "Toolbar Popup",
        {"space_type": "EMPTY", "region_type": "TEMPORARY"},
        {
            "items": [
                (
                    "wm.tool_set_by_id",
                    {"type": "SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.cursor"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_lasso"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.transform"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.measure"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Transform Modal Map",
        {"space_type": "EMPTY", "region_type": "WINDOW", "modal": True},
        {
            "items": [
                ("CONFIRM", {"type": "LEFTMOUSE", "value": "PRESS", "any": True}, None),
                ("CONFIRM", {"type": "RET", "value": "PRESS", "any": True}, None),
                (
                    "CONFIRM",
                    {"type": "NUMPAD_ENTER", "value": "PRESS", "any": True},
                    None,
                ),
                ("CANCEL", {"type": "RIGHTMOUSE", "value": "PRESS", "any": True}, None),
                ("CANCEL", {"type": "ESC", "value": "PRESS", "any": True}, None),
                ("AXIS_X", {"type": "X", "value": "PRESS"}, None),
                ("AXIS_Y", {"type": "Y", "value": "PRESS"}, None),
                ("AXIS_Z", {"type": "Z", "value": "PRESS"}, None),
                ("PLANE_X", {"type": "X", "value": "PRESS", "shift": True}, None),
                ("PLANE_Y", {"type": "Y", "value": "PRESS", "shift": True}, None),
                ("PLANE_Z", {"type": "Z", "value": "PRESS", "shift": True}, None),
                ("CONS_OFF", {"type": "C", "value": "PRESS"}, None),
                ("TRANSLATE", {"type": "W", "value": "PRESS"}, None),
                ("ROTATE", {"type": "E", "value": "PRESS"}, None),
                ("RESIZE", {"type": "R", "value": "PRESS"}, None),
                ("SNAP_TOGGLE", {"type": "TAB", "value": "PRESS", "shift": True}, None),
                (
                    "SNAP_INV_ON",
                    {"type": "LEFT_CTRL", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "SNAP_INV_OFF",
                    {"type": "LEFT_CTRL", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "SNAP_INV_ON",
                    {"type": "RIGHT_CTRL", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "SNAP_INV_OFF",
                    {"type": "RIGHT_CTRL", "value": "RELEASE", "any": True},
                    None,
                ),
                ("ADD_SNAP", {"type": "A", "value": "PRESS"}, None),
                ("REMOVE_SNAP", {"type": "A", "value": "PRESS", "alt": True}, None),
                (
                    "PROPORTIONAL_SIZE_UP",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "PROPORTIONAL_SIZE_DOWN",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    None,
                ),
                (
                    "PROPORTIONAL_SIZE_UP",
                    {"type": "PAGE_UP", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "PROPORTIONAL_SIZE_DOWN",
                    {"type": "PAGE_DOWN", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "PROPORTIONAL_SIZE_UP",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "PROPORTIONAL_SIZE_DOWN",
                    {"type": "WHEELUPMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "PROPORTIONAL_SIZE_UP",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "PROPORTIONAL_SIZE_DOWN",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                ("PROPORTIONAL_SIZE", {"type": "TRACKPADPAN", "value": "ANY"}, None),
                (
                    "EDGESLIDE_EDGE_NEXT",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "EDGESLIDE_PREV_NEXT",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "AUTOIK_CHAIN_LEN_UP",
                    {"type": "PAGE_UP", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "AUTOIK_CHAIN_LEN_DOWN",
                    {"type": "PAGE_DOWN", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "AUTOIK_CHAIN_LEN_UP",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "AUTOIK_CHAIN_LEN_DOWN",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                ("INSERTOFS_TOGGLE_DIR", {"type": "T", "value": "PRESS"}, None),
            ],
        },
    ),
    (
        "UV Editor",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "FOUR", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "VERTEX"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "EDGE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "FACE"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "FOUR", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "ISLAND"),
                        ],
                        "active": False,
                    },
                ),
                ("uv.mark_seam", {"type": "E", "value": "PRESS", "ctrl": True}, None),
                (
                    "uv.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "uv.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "uv.select_loop",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    },
                ),
                (
                    "uv.select_loop",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "uv.shortest_path_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    None,
                ),
                ("uv.select_split", {"type": "Y", "value": "PRESS"}, None),
                (
                    "uv.select_box",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("pinned", False),
                        ],
                    },
                ),
                (
                    "uv.select_box",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("pinned", True),
                        ],
                    },
                ),
                ("uv.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "uv.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "uv.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "uv.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "uv.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "uv.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", True),
                        ],
                    },
                ),
                (
                    "uv.select_more",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "uv.select_less",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "uv.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "uv.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "uv.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "uv.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "uv.select_pinned",
                    {"type": "P", "value": "PRESS", "shift": True},
                    {
                        "active": False,
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_merge"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "M", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_split"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_align"),
                        ],
                    },
                ),
                ("uv.stitch", {"type": "V", "value": "PRESS", "alt": True}, None),
                ("uv.rip_move", {"type": "V", "value": "PRESS"}, None),
                (
                    "uv.pin",
                    {"type": "P", "value": "PRESS"},
                    {
                        "properties": [
                            ("clear", False),
                        ],
                        "active": False,
                    },
                ),
                (
                    "uv.pin",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("clear", True),
                        ],
                        "active": False,
                    },
                ),
                ("uv.unwrap", {"type": "U", "value": "PRESS"}, None),
                (
                    "uv.hide",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "uv.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                ("uv.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_snap_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "TAB", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_select_mode"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "W", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                (
                    "transform.shear",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "transform.mirror",
                    {"type": "M", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_snap"),
                        ],
                    },
                ),
                (
                    "wm.context_menu_enum",
                    {"type": "TAB", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.snap_uv_element"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_context_menu"),
                        ],
                    },
                ),
                (
                    "uv.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_box"),
                            ("cycle", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "User Interface",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("ui.eyedropper_color", {"type": "I", "value": "PRESS"}, None),
                ("ui.eyedropper_colorramp", {"type": "I", "value": "PRESS"}, None),
                (
                    "ui.eyedropper_colorramp_point",
                    {"type": "I", "value": "PRESS", "alt": True},
                    None,
                ),
                ("ui.eyedropper_id", {"type": "I", "value": "PRESS"}, None),
                ("ui.eyedropper_depth", {"type": "I", "value": "PRESS"}, None),
                (
                    "ui.copy_data_path_button",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "ui.copy_data_path_button",
                    {"type": "C", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("full_path", True),
                        ],
                    },
                ),
                ("anim.keyframe_insert_button", {"type": "S", "value": "PRESS"}, None),
                (
                    "anim.keyframe_delete_button",
                    {"type": "S", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "anim.keyframe_clear_button",
                    {"type": "S", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                ("anim.driver_button_add", {"type": "D", "value": "PRESS"}, None),
                (
                    "anim.driver_button_remove",
                    {"type": "D", "value": "PRESS", "alt": True},
                    None,
                ),
                ("anim.keyingset_button_add", {"type": "K", "value": "PRESS"}, None),
                (
                    "anim.keyingset_button_remove",
                    {"type": "K", "value": "PRESS", "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Vertex Paint",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "paint.vertex_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "NORMAL"),
                        ],
                    },
                ),
                (
                    "paint.vertex_paint",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "INVERT"),
                        ],
                    },
                ),
                ("paint.brush_colors_flip", {"type": "X", "value": "PRESS"}, None),
                (
                    "brush.scale_size",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("scalar", 0.9),
                        ],
                    },
                ),
                (
                    "brush.scale_size",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("scalar", 1.1111112),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "S", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.vertex_paint.brush.size",
                            ),
                            (
                                "data_path_secondary",
                                "tool_settings.unified_paint_settings.size",
                            ),
                            (
                                "use_secondary",
                                "tool_settings.unified_paint_settings.use_unified_size",
                            ),
                            (
                                "rotation_path",
                                "tool_settings.vertex_paint.brush.texture_slot.angle",
                            ),
                            (
                                "color_path",
                                "tool_settings.vertex_paint.brush.cursor_color_add",
                            ),
                            (
                                "fill_color_path",
                                "tool_settings.vertex_paint.brush.color",
                            ),
                            (
                                "fill_color_override_path",
                                "tool_settings.unified_paint_settings.color",
                            ),
                            (
                                "fill_color_override_test_path",
                                "tool_settings.unified_paint_settings.use_unified_color",
                            ),
                            ("zoom_path", ""),
                            ("image_id", "tool_settings.vertex_paint.brush"),
                            ("secondary_tex", False),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "U", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.vertex_paint.brush.strength",
                            ),
                            (
                                "data_path_secondary",
                                "tool_settings.unified_paint_settings.strength",
                            ),
                            (
                                "use_secondary",
                                "tool_settings.unified_paint_settings.use_unified_strength",
                            ),
                            (
                                "rotation_path",
                                "tool_settings.vertex_paint.brush.texture_slot.angle",
                            ),
                            (
                                "color_path",
                                "tool_settings.vertex_paint.brush.cursor_color_add",
                            ),
                            (
                                "fill_color_path",
                                "tool_settings.vertex_paint.brush.color",
                            ),
                            (
                                "fill_color_override_path",
                                "tool_settings.unified_paint_settings.color",
                            ),
                            (
                                "fill_color_override_test_path",
                                "tool_settings.unified_paint_settings.use_unified_color",
                            ),
                            ("zoom_path", ""),
                            ("image_id", "tool_settings.vertex_paint.brush"),
                            ("secondary_tex", False),
                        ],
                    },
                ),
                (
                    "wm.radial_control",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            (
                                "data_path_primary",
                                "tool_settings.vertex_paint.brush.texture_slot.angle",
                            ),
                            ("data_path_secondary", ""),
                            ("use_secondary", ""),
                            (
                                "rotation_path",
                                "tool_settings.vertex_paint.brush.texture_slot.angle",
                            ),
                            (
                                "color_path",
                                "tool_settings.vertex_paint.brush.cursor_color_add",
                            ),
                            (
                                "fill_color_path",
                                "tool_settings.vertex_paint.brush.color",
                            ),
                            (
                                "fill_color_override_path",
                                "tool_settings.unified_paint_settings.color",
                            ),
                            (
                                "fill_color_override_test_path",
                                "tool_settings.unified_paint_settings.use_unified_color",
                            ),
                            ("zoom_path", ""),
                            ("image_id", "tool_settings.vertex_paint.brush"),
                            ("secondary_tex", False),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TRANSLATION"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "SCALE"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ROTATION"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "TRANSLATION"),
                            ("texmode", "SECONDARY"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {
                        "type": "RIGHTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SCALE"),
                            ("texmode", "SECONDARY"),
                        ],
                    },
                ),
                (
                    "brush.stencil_control",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ROTATION"),
                            ("texmode", "SECONDARY"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "vertex_paint_object.data.use_paint_mask"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            (
                                "data_path",
                                "tool_settings.vertex_paint.brush.use_smooth_stroke",
                            ),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "R", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_angle_control"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_paint_vertex_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_paint_vertex_context_menu"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "D", "value": "PRESS"},
                    {
                        "properties": [
                            ("vertex_tool", "DRAW"),
                        ],
                    },
                ),
                (
                    "paint.brush_select",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("vertex_tool", "BLUR"),
                        ],
                        "active": False,
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "Q", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_box"),
                            ("cycle", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Window",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.batch_rename",
                    {"type": "RET", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "wm.read_homefile",
                    {"type": "N", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "O", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", "TOPBAR_MT_file_open_recent"),
                        ],
                    },
                ),
                (
                    "wm.open_mainfile",
                    {"type": "O", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.save_mainfile",
                    {"type": "S", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.save_as_mainfile",
                    {"type": "S", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "wm.quit_blender",
                    {"type": "Q", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "SCREEN_MT_user_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "NDOF_BUTTON_MENU", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "USERPREF_PT_ndof_settings"),
                        ],
                    },
                ),
                (
                    "wm.context_scale_float",
                    {"type": "NDOF_BUTTON_PLUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "preferences.inputs.ndof_sensitivity"),
                            ("value", 1.1),
                        ],
                    },
                ),
                (
                    "wm.context_scale_float",
                    {"type": "NDOF_BUTTON_MINUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "preferences.inputs.ndof_sensitivity"),
                            ("value", 0.90909094),
                        ],
                    },
                ),
                (
                    "wm.context_scale_float",
                    {"type": "NDOF_BUTTON_PLUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "preferences.inputs.ndof_sensitivity"),
                            ("value", 1.5),
                        ],
                    },
                ),
                (
                    "wm.context_scale_float",
                    {"type": "NDOF_BUTTON_MINUS", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "preferences.inputs.ndof_sensitivity"),
                            ("value", 0.6666667),
                        ],
                    },
                ),
                (
                    "info.reports_display_update",
                    {"type": "TIMER_REPORT", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "TWO", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "space_data.overlay.show_wireframes"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "EIGHT", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "scene.tool_settings.sculpt.use_symmetry_x"),
                        ],
                    },
                ),
                (
                    "wm.context_menu_enum",
                    {"type": "SIX", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "space_data.shading.type"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.lock_camera"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "P", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "space_data.overlay.show_floor"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("data_path", "space_data.overlay.show_extras"),
                        ],
                    },
                ),
            ],
        },
    ),
]


if __name__ == "__main__":
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data

    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0], keyconfig_data
    )
