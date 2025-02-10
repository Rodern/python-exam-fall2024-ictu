using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using System.Collections.Generic;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IMessageService
    {
        Task<Message> SendMessageAsync(MessageDto messageDto);
        Task<IEnumerable<Message>> GetMessagesAsync(int conversationId);
        Task SendMediaAsync(int conversationId, string mediaUrl);
    }
}
