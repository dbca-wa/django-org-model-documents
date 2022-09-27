===================
Org Model Documents
===================

Org model documents is a Django app created for DBCA to allow developers to attach documents to
any model in their project without having to duplicate a lot of code.

Quick start
-----------

1. Add "org_model_documents" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'org_model_documents',
    ]

2. You can include the org_model_documents URLconf in your project urls.py like this:

    path('org-model-documents/', include('org_model_documents.urls')),

    however it's more likely you will need to apply specific permissions to the org_model_documents api end-points,
    therefor it is recommended to create subclasses of the viewsets within your own project and add urls
    for those to your own project also:

    i.e. To allow uploading of documents only by internal users add the following into your
    yourproject/components/main/api.py file:

    from org_model_documents.api import (
        DocumentCreateView,
    )   

    from yourproject.permissions import IsInternal, etc..

    class DocumentCreateView(DocumentCreateView):
        permission_classes = [IsInternal]

    Then create a url in your project that uses that view.

3. Run ``python manage.py migrate`` to create the org model documents models.
