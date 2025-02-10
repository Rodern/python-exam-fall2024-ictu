using ChatMateServerApp.Dtos;
using ChatMateServerApp.DbServices.Interfaces;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/groups")]
    public class GroupsController : ControllerBase
    {
        private readonly IGroupService _groupService;

        public GroupsController(IGroupService groupService)
        {
            _groupService = groupService;
        }

        // POST: api/groups
        [HttpPost]
        [Authorize]
        public IActionResult CreateGroup([FromBody] GroupDto groupDto)
        {
            var result = _groupService.CreateGroup(groupDto);
            return Ok(result);
        }

        // GET: api/groups/{groupId}
        [HttpGet("{groupId}")]
        [Authorize]
        public IActionResult GetGroup(int groupId)
        {
            var group = _groupService.GetGroup(groupId);
            return Ok(group);
        }

        // PUT: api/groups/{groupId}
        [HttpPut("{groupId}")]
        [Authorize]
        public IActionResult UpdateGroup(int groupId, [FromBody] GroupDto groupDto)
        {
            var result = _groupService.UpdateGroup(groupId, groupDto);
            return Ok(result);
        }

        // DELETE: api/groups/{groupId}
        [HttpDelete("{groupId}")]
        [Authorize]
        public IActionResult DeleteGroup(int groupId)
        {
            var result = _groupService.DeleteGroup(groupId);
            return Ok(result);
        }

        // POST: api/groups/{groupId}/members
        [HttpPost("{groupId}/members")]
        [Authorize]
        public IActionResult AddMember(int groupId, [FromBody] GroupMemberDto memberDto)
        {
            var result = _groupService.AddMember(groupId, memberDto.UserId);
            return Ok(result);
        }

        // DELETE: api/groups/{groupId}/members/{memberId}
        [HttpDelete("{groupId}/members/{memberId}")]
        [Authorize]
        public IActionResult RemoveMember(int groupId, int memberId)
        {
            var result = _groupService.RemoveMember(groupId, memberId);
            return Ok(result);
        }
    }
}
