using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using System.Collections.Generic;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IGroupService
    {
        Task<Group> CreateGroupAsync(GroupDto groupDto);
        Task<Group> GetGroupAsync(int groupId);
        Task UpdateGroupAsync(int groupId, GroupDto groupDto);
        Task DeleteGroupAsync(int groupId);
        Task AddMemberAsync(int groupId, int userId);
        Task RemoveMemberAsync(int groupId, int userId);
    }
}
