using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using System.Collections.Generic;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IStatusService
    {
        Task<Status> PostStatusAsync(StatusDto statusDto);
        Task<IEnumerable<Status>> GetStatusUpdatesAsync(int userId);
        Task DeleteStatusAsync(int statusId);
    }
}
