using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace ChatMateServerApp.DbModels
{
    public class User
    {
        public int UserId { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string UserName { get; set; }
        public string PhoneNumber { get; set; } // Used as password for simplicity
        public string ProfilePictureUrl { get; set; }

        public ICollection<Message> MessagesSent { get; set; }
        public ICollection<Message> MessagesReceived { get; set; }
        public ICollection<Status> StatusUpdates { get; set; }
        public ICollection<Group> Groups { get; set; }
    }
}
