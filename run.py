# posts = [
#     {
#         'author': "Ben",
#         'title': "First Title",
#         'content': "First Post Content",
#         'date_posted': "December 27, 2020"
#     },
#     {
#         'author': "Ben",
#         'title': "Second Title",
#         'content': "Second Post Content",
#         'date_posted': "December 27, 2020"
#     },
# ]

from blog import app

if __name__ == '__main__':
    app.run(debug=True)