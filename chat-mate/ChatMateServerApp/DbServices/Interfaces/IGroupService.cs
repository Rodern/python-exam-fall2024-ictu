using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using System.Collections.Generic;
using ChatMateServerApp.Data;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IGroupService
    {
        RequestResponse CreateGroup(GroupDto groupDto);
        RequestResponse GetGroup(int groupId);
        RequestResponse UpdateGroup(int groupId, GroupDto groupDto);
        RequestResponse DeleteGroup(int groupId);
        RequestResponse AddMember(int groupId, int userId);
        RequestResponse RemoveMember(int groupId, int userId);
    }
}
