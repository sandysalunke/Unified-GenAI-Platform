from ui.components import text_component, image_component, meeting_component, excel_component

'''
def route(request_type, input_data):
    
    if request_type == 'audio':
        return audio_service.handle_request(input_data)
    elif request_type == 'image':
        return image_service.handle_request(input_data)
    elif request_type == 'text':
        return text_service.handle_request(input_data)
    elif request_type == 'meeting':
        return meeting_service.handle_request(input_data)
    elif request_type == 'excel':
        return data_service.handle_request(input_data)
    else:
        return "Invalid request type", 400
'''

def route(request_type):
    if request_type == 'text':
        return text_component.render()
    elif request_type == 'image':
        return image_component.render()
    elif request_type == 'meeting':
        return meeting_component.render()
    elif request_type == 'excel':
        return excel_component.render()
    else:
        return "Invalid request type", 400