from decouple import config

API_ACCESS = config("ACCESS_KEY")
API_SECRET = config("SECRET_KEY")
test_api_keys = (API_ACCESS, API_SECRET)
test_did = "8346754b889488737d2a8e6f"
test_wid = "4e2d3b3e96337549279a990c"
test_eid_empty = "1e870da4963223b91567fe68"
test_eid_with_data = "e9989d4fab94ba77afdeed55"
get_scope_eid = "99cf0d68f304228bd62800ca"
set_scope_eid = "38b460aac3d498391a3695be"
get_references_eid = "ec3fece406061218ba0465f7"
append_references_eid = "957bd9d7d3d9ce72cdc121ee"
replace_references_eid = "73bd0c13adc884364414b557"

replace_variables_eid = "058cbbb6508b59283d0f4e5e"
append_variables_eid = "0648d0c6a71d9ab936cfc865"


variables_with_value = [
    {
        "name": "FRAME_LEN",
        "value": None,
        "type": "LENGTH",
        "description": "steel frame length",
        "expression": "150 mm",
    },
    {
        "name": "FRAME_ST_ANG",
        "value": None,
        "type": "ANGLE",
        "description": "frame stems angle",
        "expression": "90 deg",
    },
    {
        "name": "FRAME_OUT_SQ",
        "value": None,
        "type": "LENGTH",
        "description": "frame outer square",
        "expression": "20 mm",
    },
    {
        "name": "FRAME_IN_SQ",
        "value": None,
        "type": "LENGTH",
        "description": "frame inner square",
        "expression": "7.8 mm",
    },
    {
        "name": "FRAME_ST_NUM",
        "value": None,
        "type": "NUMBER",
        "description": "number of frame stems",
        "expression": "4",
    },
]
variables_without_value = [
    {k: v for k, v in variable.items() if k != "value"}
    for variable in variables_with_value
]


references_exists = {
    "references": [
        {
            "variableNames": [],
            "entireVariableStudio": True,
            "referenceDocumentId": "",
            "referenceVersionId": "",
            "referenceElementId": "e9989d4fab94ba77afdeed55",
        }
    ]
}
