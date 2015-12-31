# import_export_vote_smart/views_admin.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from .controllers import retrieve_vote_smart_candidates_into_local_db, retrieve_vote_smart_candidate_bio_into_local_db, \
    retrieve_vote_smart_officials_into_local_db, retrieve_and_save_vote_smart_states
from .models import VoteSmartState
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render


def import_states_view(request):
    """
    """
    # # If person isn't signed in, we don't want to let them visit this page yet
    # if not request.user.is_authenticated():
    #     return redirect('/admin')

    retrieve_and_save_vote_smart_states()

    template_values = {
        'state_list': VoteSmartState.objects.order_by('name'),
    }
    return render(request, 'import_export_vote_smart/vote_smart_import.html', template_values)


def import_photo_view(request):
    # NOTE: This view is for testing purposes. For the operational "Import Vote Smart Images" view, see:
    #  "candidate_retrieve_photos_view" in candidate/views_admin.py
    last_name = "Trump"
    results = retrieve_vote_smart_candidates_into_local_db(last_name)
    if not results['success']:
        messages.add_message(request, messages.INFO, results['status'])
    else:
        messages.add_message(request, messages.INFO, "Photo retrieved.")

        # Now we can go on to make sure we have the right VoteSmartCandidate
        vote_smart_candidate_id = 15723
        # ...and then retrieve the photo
        results = retrieve_vote_smart_candidate_bio_into_local_db(vote_smart_candidate_id)

    last_name = "Pelosi"
    results = retrieve_vote_smart_officials_into_local_db(last_name)

    messages_on_stage = get_messages(request)

    template_values = {
        'messages_on_stage': messages_on_stage,
    }
    return render(request, 'import_export_vote_smart/vote_smart_import.html', template_values)


def state_detail_view(request, pk):
    """
    """
    # # If person isn't signed in, we don't want to let them visit this page yet
    # if not request.user.is_authenticated():
    #     return redirect('/admin')
    state_id = pk

    template_values = {
        'state': VoteSmartState.objects.get(stateId=state_id),
    }
    return render(request, 'import_export_vote_smart/state_detail.html', template_values)
