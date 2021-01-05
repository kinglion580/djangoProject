from redis import StrictRedis
import json

# Function to add new notifications for user
def add_notification(user_id, notification_id, data):
    r = StrictRedis(host='localhost', port=6379)
    r.hset('%s_notifications' % user_id, notification_id, json.dumps(data))

# Function to set the notification as read, your Frontend looks at the "read" key in
# Notification's data to determine how to show the notification
def set_notification_as_read(user_id, notification_id):
    r = StrictRedis(host='localhost', port=6379)
    data = json.loads(r.hget('%s_notifications' % user_id, notification_id))
    data['read'] = True
    add_notification(user_id, notification_id, data)

# Gets all notifications for a user, you can sort them based on a key like "date" in Frontend
def get_notifications(user_id):
    r = StrictRedis(host='localhost', port=6379)
    return r.hgetall('%s_notifications' % user_id)