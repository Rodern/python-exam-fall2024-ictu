using ChatMateServerApp.Dtos;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/groups")]
    public class GroupsController : ControllerBase
    {
        // POST: api/groups
        [HttpPost]
        [Authorize]
        public IActionResult CreateGroup([FromBody] GroupDto groupDto)
        {
            // Create group logic here
            return Ok();
        }

        // GET: api/groups/{groupId}
        [HttpGet("{groupId}")]
        [Authorize]
        public IActionResult GetGroup(Guid groupId)
        {
            // Retrieve group info logic here
            return Ok();
        }

        // PUT: api/groups/{groupId}
        [HttpPut("{groupId}")]
        [Authorize]
        public IActionResult UpdateGroup(Guid groupId, [FromBody] GroupDto groupDto)
        {
            // Update group info logic here
            return Ok();
        }

        // DELETE: api/groups/{groupId}
        [HttpDelete("{groupId}")]
        [Authorize]
        public IActionResult DeleteGroup(Guid groupId)
        {
            // Delete group logic here
            return Ok();
        }

        // POST: api/groups/{groupId}/members
        [HttpPost("{groupId}/members")]
        [Authorize]
        public IActionResult AddMember(Guid groupId, [FromBody] GroupMemberDto memberDto)
        {
            // Add member logic here
            return Ok();
        }

        // DELETE: api/groups/{groupId}/members/{memberId}
        [HttpDelete("{groupId}/members/{memberId}")]
        [Authorize]
        public IActionResult RemoveMember(Guid groupId, Guid memberId)
        {
            // Remove member logic here
            return Ok();
        }
    }
}
