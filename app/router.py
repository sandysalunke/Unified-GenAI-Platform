from ui.components import text_component, image_component, meeting_component, excel_component, image2text_component, dbsearch_component, rdbsearch_component

def route(request_type):
    if request_type == 'text':
        return text_component.render()
    elif request_type == 'image':
        return image_component.render()
    elif request_type == 'meeting':
        return meeting_component.render()
    elif request_type == 'excel':
        return excel_component.render()
    elif request_type == 'image2text':
        return image2text_component.render()
    elif request_type == 'DBSearch':
        return dbsearch_component.render()
    elif request_type == 'RDBSearch':
        return rdbsearch_component.render()
    else:
        return "Invalid request type", 400