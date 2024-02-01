// Workshop 8 - Smart Pointers

#include <memory>
#include <utility>
#include "DataBase.h"
#include "Profile.h"
#include "Utilities.h"

using namespace std;

namespace sdds {
	DataBase<Profile> excludeRaw(const DataBase<Profile>& allProfiles, const DataBase<Profile>& bannedProfiles) {
		DataBase<Profile> result;
		// TODO: Add your code here to build a collection of Profiles.
		//		   The result should contain only profiles from `allProfiles`
		//         which are not in `bannedProfiles` using Raw Pointers.
		for (int i = 0; i < allProfiles.size(); i++){
			for (int j = 0; j < bannedProfiles.size(); j++){
				string a_name = allProfiles[i].m_name.first_name + allProfiles[i].m_name.last_name;
				int a_age = allProfiles[i].m_age;
				string b_name = bannedProfiles[j].m_name.first_name + bannedProfiles[j].m_name.last_name;
				int b_age = bannedProfiles[j].m_age;

				if(a_name == b_name && a_age == b_age){
					break;
				}
				else{ 
					Profile* ptr;
					ptr = new Profile;
					ptr->m_address = allProfiles[i].m_address;
					if(ptr->validateAddress()){
						result += allProfiles[i];
					}
					else{}
					delete ptr;	
				}
				
			}
		}




		return result;
	}
	
	DataBase<Profile> excludeSmart(const DataBase<Profile>& allProfiles, const DataBase<Profile>& bannedProfiles) {
		DataBase<Profile> result;
		// TODO: Add your code here to build a collection of Profiles.
		//		   The result should contain only profiles from `allProfiles`
		//         which are not in `bannedProfiles` using Smart Pointers.
		for (int i = 0; i < allProfiles.size(); i++){
			for (int j = 0; j < bannedProfiles.size(); j++){
				string a_name = allProfiles[i].m_name.first_name + allProfiles[i].m_name.last_name;
				int a_age = allProfiles[i].m_age;
				string b_name = bannedProfiles[j].m_name.first_name + bannedProfiles[j].m_name.last_name;
				int b_age = bannedProfiles[j].m_age;

				if(a_name == b_name && a_age == b_age){
					break;
				}
				else{ 
					std::unique_ptr<Profile> ptr(new Profile);
					ptr->m_address = allProfiles[i].m_address;
					if(ptr->validateAddress()){
						result += allProfiles[i];
					}
					else{}	
				}
				
			}
		}





		return result;
	}
}
