
import praw
from bs4 import BeautifulSoup


reddit_client_id = 'client_id'
reddit_client_secret = 'client_secret'
# reddit_username = ''
# reddit_password = ''
reddit_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'


# Initialize Reddit API
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent
)

def get_reddit_thread_info(thread_url):
    submission = reddit.submission(url=thread_url)
    submission_comments = submission.comments.list()

    # Generate HTML document
    html_doc = f'<html><head><title>{submission.title}</title></head><body>'
    html_doc += f'<h1>{submission.title}</h1>'
    
    for comment in submission_comments:
        html_doc += format_comment(comment, level=0)

    html_doc += '</body></html>'
    return html_doc

def format_comment(comment, level):
    indent_size = 20
    indent = ' ' * (level * indent_size)
    
    html_comment = f'{indent}<div style="padding: 10px; border: 1px solid #ddd; margin: 10px; background-color: #f9f9f9;">'
    html_comment += f'<p style="margin: 0;"><strong>{comment.author.name}</strong> - Score: {comment.score}</p>'
    html_comment += f'<p>{comment.body}</p>'
    
    for reply in comment.replies:
        html_comment += format_comment(reply, level + 1)
    
    html_comment += f'{indent}</div>'
    return html_comment

if __name__ == "__main__":
    thread_url = input("Enter the Reddit thread URL: ")
    html_content = get_reddit_thread_info(thread_url)

    with open("reddit_thread.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print("HTML file generated successfully. Check 'reddit_thread.html'.")
