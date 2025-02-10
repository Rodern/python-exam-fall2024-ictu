using ChatMateServerApp.DbModels;
using ChatMateServerApp.DbServices.Interfaces;
using ChatMateServerApp.Dtos;
using Microsoft.EntityFrameworkCore;
using ChatMateServerApp.Data;
using Newtonsoft.Json;

namespace ChatMateServerApp.DbServices
{
    public class GroupService : IGroupService
    {
        private readonly ChatMateContext _context;

        public GroupService(ChatMateContext context)
        {
            _context = context;
        }

        public RequestResponse CreateGroup(GroupDto groupDto)
        {
            var group = new Group
            {
                Name = groupDto.Name,
                Description = groupDto.Description,
                GroupPictureUrl = groupDto.GroupPictureUrl,
                Members = new List<User>()
            };

            _context.Groups.Add(group);
            _context.SaveChanges();
            return new RequestResponse { Data = JsonConvert.SerializeObject(group), Success = true };
        }

        public RequestResponse GetGroup(int groupId)
        {
            var group = _context.Groups
                .Include(g => g.Members)
                .FirstOrDefault(g => g.GroupId == groupId);
            return new RequestResponse { Data = JsonConvert.SerializeObject(group), Success = group != null };
        }

        public RequestResponse UpdateGroup(int groupId, GroupDto groupDto)
        {
            var group = _context.Groups.Find(groupId);
            if (group == null) return new RequestResponse { Success = false, Message = "Group not found" };

            group.Name = groupDto.Name;
            group.Description = groupDto.Description;
            group.GroupPictureUrl = groupDto.GroupPictureUrl;

            _context.Groups.Update(group);
            _context.SaveChanges();
            return new RequestResponse { Success = true };
        }

        public RequestResponse DeleteGroup(int groupId)
        {
            var group = _context.Groups.Find(groupId);
            if (group == null) return new RequestResponse { Success = false, Message = "Group not found" };

            _context.Groups.Remove(group);
            _context.SaveChanges();
            return new RequestResponse { Success = true };
        }

        public RequestResponse AddMember(int groupId, int userId)
        {
            var group = _context.Groups
                .Include(g => g.Members)
                .FirstOrDefault(g => g.GroupId == groupId);
            if (group == null) return new RequestResponse { Success = false, Message = "Group not found" };

            var user = _context.Users.Find(userId);
            if (user == null) return new RequestResponse { Success = false, Message = "User not found" };

            group.Members.Add(user);
            _context.SaveChanges();
            return new RequestResponse { Success = true };
        }

        public RequestResponse RemoveMember(int groupId, int userId)
        {
            var group = _context.Groups
                .Include(g => g.Members)
                .FirstOrDefault(g => g.GroupId == groupId);
            if (group == null) return new RequestResponse { Success = false, Message = "Group not found" };

            var user = group.Members.FirstOrDefault(m => m.UserId == userId);
            if (user == null) return new RequestResponse { Success = false, Message = "User not found in group" };

            group.Members.Remove(user);
            _context.SaveChanges();
            return new RequestResponse { Success = true };
        }
    }
}
