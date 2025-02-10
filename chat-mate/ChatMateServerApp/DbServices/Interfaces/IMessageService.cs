using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using System.Collections.Generic;
using ChatMateServerApp.Data;
using System.Collections.ObjectModel;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IMessageService
    {
        RequestResponse SendMessage(MessageDto messageDto);
        ObservableCollection<Message> GetMessages(int conversationId);
        RequestResponse SendMedia(int conversationId, string mediaUrl);
    }
}
