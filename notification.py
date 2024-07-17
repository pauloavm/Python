"""
Utilize para exibir uma notificação na taskbar do Windows( só testei no Windows 11)
"""

# pip install plyer


from plyer import notification

# Display a notification

notification.notify(
    title='Hello',
    message='Hello, Take a Break',
    app_name='Python Clcoding'

)
