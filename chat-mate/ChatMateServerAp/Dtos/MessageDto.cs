namespace ChatMateServerAp.Dtos
{
    public class MessageDto
    {
        public string Content { get; set; }
        public DateTime Timestamp { get; set; }
        public int SenderId { get; set; }
        public int ReceiverId { get; set; }
        public int? GroupId { get; set; }
    }
}
