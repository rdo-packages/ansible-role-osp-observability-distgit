%global srcname osp_observability_ansible
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global tarsources osp-observability-ansible

Name:           ansible-osp-observability
Version:        XXX
Release:        XXX
Summary:        Ansible collection for deploying observability components in OSP
License:        ASL 2.0
URL:            https://www.github.com/infrawatch/osp-observability-ansible
Source0:        https://github.com/infrawatch/osp-observability-ansible/archive/%{upstream_version}/osp-observability-ansible-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core

Requires:       (python3dist(ansible) or ansible-core)

%description
Ansible collection for deploying observability components with TripleO

%prep
# Using this suggestion, I see now that it is actually being used in zuul, but I'm not sure where this is actually being set; or how to make it so I can build it locally.
%autosetup -n ansible-role-osp-observability-%{upstream_version} -S git

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible/collections/ansible_collections/infrawatch
cp -r ./* %{buildroot}%{_datadir}/ansible/collections/ansible_collections/infrawatch

%files
%doc README*
%license LICENSE
%{_datadir}/ansible/collections/ansible_collections/infrawatch/

%changelog

