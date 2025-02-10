

namespace ChatMateServerApp.DbModels
{
    public class Message
    {
        public int MessageId { get; set; }
        public string Content { get; set; }
        public DateTime Timestamp { get; set; }

        public int SenderId { get; set; }
        public User Sender { get; set; }

        public int ReceiverId { get; set; }
        public User Receiver { get; set; }

        public int? GroupId { get; set; }
        public Group Group { get; set; }
    }
}
