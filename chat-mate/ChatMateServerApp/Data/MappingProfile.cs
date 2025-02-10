using AutoMapper;
using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;

namespace ChatMateServerApp.Data
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            // User Mappings
            CreateMap<User, UserRegistrationDto>().ReverseMap();
            CreateMap<User, UserLoginDto>().ReverseMap();
            CreateMap<User, UserProfileDto>().ReverseMap();

            // Message Mappings
            CreateMap<Message, MessageDto>().ReverseMap();

            // Status Mappings
            CreateMap<Status, StatusDto>().ReverseMap();

            // Group Mappings
            CreateMap<Group, GroupDto>().ReverseMap();
            CreateMap<GroupMemberDto, User>()
                .ForMember(dest => dest.UserId, opt => opt.MapFrom(src => src.UserId))
                .ReverseMap();
        }
    }
}
