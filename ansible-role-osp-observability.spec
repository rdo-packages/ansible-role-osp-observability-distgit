%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Required for ansible_collection_* macros
%global collection_name osp_observability
%global collection_namespace infrawatch

Name:           ansible-osp-observability
Version:        XXX
Release:        XXX
Summary:        Ansible collection for deploying observability components in OSP
License:        ASL 2.0
URL:            https://www.github.com/infrawatch/osp-observability-ansible
Source0:        https://github.com/infrawatch/osp-observability-ansible/archive/%{upstream_version}/osp-observability-ansible-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  (python3dist(ansible) or ansible-core)

Requires:       (python3dist(ansible) or ansible-core)

%description
Ansible collection for deploying observability components with TripleO

%prep
%autosetup -n ansible-role-osp-observability-%{upstream_version} -S git
# Remove dotfiles

%build
sed -ie 's/\(version: \)\(.*\)$/\1%{version}/g' galaxy.yml
%{ansible_collection_build}

%install
%{ansible_collection_install}

%files
%doc README*
%license LICENSE
%{ansible_collection_files}

%changelog

