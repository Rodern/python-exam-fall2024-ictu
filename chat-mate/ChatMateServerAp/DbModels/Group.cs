namespace ChatMateServerAp.DbModels
{
    public class Group
    {
        public int GroupId { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string GroupPictureUrl { get; set; }

        public ICollection<User> Members { get; set; }
        public ICollection<Message> Messages { get; set; }
    }
}
