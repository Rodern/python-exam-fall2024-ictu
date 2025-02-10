using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using System.Collections.Generic;
using ChatMateServerApp.Data;
using System.Collections.ObjectModel;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IStatusService
    {
        RequestResponse PostStatus(StatusDto statusDto);
        ObservableCollection<Status> GetStatusUpdates(int userId);
        RequestResponse DeleteStatus(int statusId);
    }
}
