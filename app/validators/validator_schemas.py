user_schema = {
  "first_name": {
    "type": "string",
    "required": True
  },
  "last_name": {
    "type": "string",
    "required": True
  },
  "mobile_number": {
    "type": "string",
    "required": True
  },
  "profilePic": {
    "type": "string"
  },
  "location": {
    "type": "dict",
    "schema": {
      "country": {
        "type": "string"
      },
      "state": {
        "type": "string"
      },
      "district": {
        "type": "string"
      }
    }
  }
}


post_schema = {
 "data": {
    "type": "list",
    "schema": {
      "type": "dict",
      "schema": {
        "data_type": {
          "type": "string"
        },
        "data": {
          "type": "list",
          "schema": {
            "type": "dict",
            "schema": {
              "data_info_type": {
                "type": "string"
              },
              "value": {
                "type": "string"
              }
            }
          }
        }
      }
    }
  }
}


