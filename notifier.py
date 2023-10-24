
def notify(title="Notification",body=("Notification body",)):
    from win10toast import ToastNotifier
    toast = ToastNotifier()
    body = "\n".join(body)
    toast.show_toast(title,body,icon_path="assets/icon.ico",duration=20)
    help(toast.show_toast)

title = input("Title: ")
body = [input(f"line {i+1}: ") for i in range( int(input("Total no. of lines: ")) )]
notify(title,body)

