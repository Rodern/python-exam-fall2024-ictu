using ChatMateServerApp.DbModels;
using ChatMateServerApp.DbServices.Interfaces;
using ChatMateServerApp.Dtos;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace ChatMateServerApp.DbServices
{
    public class GroupService : IGroupService
    {
        private readonly ChatMateContext _context;

        public GroupService(ChatMateContext context)
        {
            _context = context;
        }

        public async Task<Group> CreateGroupAsync(GroupDto groupDto)
        {
            var group = new Group
            {
                Name = groupDto.Name,
                Description = groupDto.Description,
                GroupPictureUrl = groupDto.GroupPictureUrl,
                Members = new List<User>()
            };

            _context.Groups.Add(group);
            await _context.SaveChangesAsync();
            return group;
        }

        public async Task<Group> GetGroupAsync(int groupId)
        {
            return await _context.Groups
                .Include(g => g.Members)
                .FirstOrDefaultAsync(g => g.GroupId == groupId);
        }

        public async Task UpdateGroupAsync(int groupId, GroupDto groupDto)
        {
            var group = await _context.Groups.FindAsync(groupId);
            if (group == null) throw new Exception("Group not found");

            group.Name = groupDto.Name;
            group.Description = groupDto.Description;
            group.GroupPictureUrl = groupDto.GroupPictureUrl;

            _context.Groups.Update(group);
            await _context.SaveChangesAsync();
        }

        public async Task DeleteGroupAsync(int groupId)
        {
            var group = await _context.Groups.FindAsync(groupId);
            if (group == null) throw new Exception("Group not found");

            _context.Groups.Remove(group);
            await _context.SaveChangesAsync();
        }

        public async Task AddMemberAsync(int groupId, int userId)
        {
            var group = await _context.Groups
                .Include(g => g.Members)
                .FirstOrDefaultAsync(g => g.GroupId == groupId);
            if (group == null) throw new Exception("Group not found");

            var user = await _context.Users.FindAsync(userId);
            if (user == null) throw new Exception("User not found");

            group.Members.Add(user);
            await _context.SaveChangesAsync();
        }

        public async Task RemoveMemberAsync(int groupId, int userId)
        {
            var group = await _context.Groups
                .Include(g => g.Members)
                .FirstOrDefaultAsync(g => g.GroupId == groupId);
            if (group == null) throw new Exception("Group not found");

            var user = group.Members.FirstOrDefault(m => m.UserId == userId);
            if (user == null) throw new Exception("User not found in group");

            group.Members.Remove(user);
            await _context.SaveChangesAsync();
        }
    }
}
