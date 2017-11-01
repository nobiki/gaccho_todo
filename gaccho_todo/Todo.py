from Article import Article

class Todo(Article):
    def color_pair(self):
        return {"text":"YELLOW", "back":"CYAN"}

    def get(self):

        return [
                ("Todo", "2017-10-19 10:00:00", "投稿者名", "あれやる", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("Todo", "2017-10-20 10:00:01", "投稿者名", "これやる", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("Todo", "2017-10-21 10:00:02", "投稿者名", "あれもこれもやるはvalueとおなじ", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("Todo", "2017-10-22 10:00:00", "投稿者名", "あれやって", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("Todo", "2017-10-19 10:00:01", "投稿者名", "これやって", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("Todo", "2017-10-27 10:00:02", "投稿者名", "あれとこれやって", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ("Todo", "2017-10-19 10:00:02", "投稿者名", "やっぱりこれも", "http://example.com/", "てきすとてきすとてきすとてきすと"),
                ]
