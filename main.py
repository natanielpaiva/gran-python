from database import Database
from models import Post
from sentiment_analysis import analyze_sentiment

def main():
    db = Database('twitter.db')

    # Exemplo de posts
    posts = [
        "I love Python! Is the best programming language!",
        "I Dont like others programming languages",
        "Python is really"
    ]

    for text in posts:
        category = analyze_sentiment(text)
        post = Post(text, category)
        db.insert_post(post.post, post.category)

    for post in db.read_posts():
        print(f'Post: {post[1]}, Categoria: {post[2]}')

if __name__ == '__main__':
    main()
