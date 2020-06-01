def app(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = '\n'.join(env.split('&'))

    start_response(status, headers)
    return [body]
