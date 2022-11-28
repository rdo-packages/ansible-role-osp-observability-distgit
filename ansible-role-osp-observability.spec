%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global tarsources osp-observability-ansible
%global upstream_version efoley-galaxy_add_build_ignore
# Required for ansible_collection_* macros
%global collection_name osp_observability
%global collection_namespace infrawatch

Name:           ansible-osp-observability
Version:        0.0.2
Release:        1%{?dist}
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
%autosetup -n %{tarsources}-%{upstream_version} -S git

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

