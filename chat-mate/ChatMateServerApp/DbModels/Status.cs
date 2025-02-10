namespace ChatMateServerApp.DbModels
{
    public class Status
    {
        public int StatusId { get; set; }
        public string Content { get; set; }
        public DateTime Timestamp { get; set; }
        public string MediaUrl { get; set; }

        public int UserId { get; set; }
        public User User { get; set; }
    }
}
