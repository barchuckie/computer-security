def parse(request):
    request = request.split()

    result = {}
    for data in request:
        if 'PHPSESSID' in data:
            session = data.replace(';', '')
            session_id = session.split('=')
            result[session_id[0]] = session_id[1]

    return result
