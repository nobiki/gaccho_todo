from Article import Article

from datetime import datetime
from time import mktime

class Todo(Article):
    def color_pair(self):
        return {"text":"BLACK", "back":"YELLOW"}

    def get(self):

        return [
                ("ToDo", "2017-10-19 10:00:00", "投稿者名", "あれをやる", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("ToDo", "2017-10-20 10:00:01", "投稿者名", "これをやる", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("ToDo", "2017-10-21 10:00:02", "投稿者名", "あれもやる", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("ToDo", "2017-10-22 10:00:00", "投稿者名", "これもやる", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("ToDo", "2017-10-19 10:00:01", "投稿者名", "あれもこれもやる", "http://example.com/", "てきすとてきすとてきすとてきすと")
                ]
