# apis_v1/documentation_source/voter_plan_save_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def voter_plan_save_doc_template_values(url_root):
    """
    Show documentation about voterPlanSave
    """
    required_query_parameter_list = [
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
        {
            'name':         'google_civic_election_id',
            'value':        'integer',  # boolean, integer, long, string
            'description':  'Limit results to this election',
        },
        {
            'name':         'voter_device_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'An 88 character unique identifier linked to a voter record on the server. ',
        },
        {
            'name':         'voter_plan_data_serialized',
            'value':        'string',  # boolean, integer, long, string
            'description':  '',
        },
        {
            'name':         'voter_plan_text',
            'value':        'string',  # boolean, integer, long, string
            'description':  '',
        },
        {
            'name':         'show_to_public',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  '',
        },
    ]

    optional_query_parameter_list = [
    ]

    potential_status_codes_list = [
        {
            'code':         'VALID_VOTER_DEVICE_ID_MISSING',
            'description':  'A valid voter_device_id parameter was not included. Cannot proceed.',
        },
        {
            'code':         'VOTER_NOT_FOUND_FROM_VOTER_DEVICE_ID',
            'description':  'No voter could be found from the voter_device_id',
        },
    ]

    try_now_link_variables_dict = {
        # 'voter_device_id': '',
    }

    api_response = '{\n' \
                   '  "success": boolean,\n' \
                   '  "status": string,\n' \
                   '  "voter_plan_list": list\n' \
                   '   [{\n' \
                   '     "google_civic_election_id": integer,\n' \
                   '     "state_code": string,\n' \
                   '     "voter_display_name": string,\n' \
                   '     "voter_display_city_state": string,\n' \
                   '     "voter_we_vote_id": string,\n' \
                   '     "voter_plan_data_serialized": string,\n' \
                   '     "voter_plan_text": string,\n' \
                   '     "show_to_public": boolean,\n' \
                   '     "date_entered": string,\n' \
                   '     "date_last_changed": string,\n' \
                   '     "we_vote_hosted_profile_image_url_medium": string,\n' \
                   '   },],\n' \
                   '}'

    template_values = {
        'api_name': 'voterPlanSave',
        'api_slug': 'voterPlanSave',
        'api_introduction':
            "Save a voter_plan for one voter.",
        'try_now_link': 'apis_v1:voterPlanSaveView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
