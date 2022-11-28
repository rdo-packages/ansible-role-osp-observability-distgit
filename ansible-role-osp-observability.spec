%global srcname osp_observability_ansible
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global tarsources osp-observability-ansible

Name:           ansible-osp-observability
Version:        0.0.2
Release:        1%{?dist}
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
%autosetup -n %{tarsources}-%{upstream_version} -S git

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible/collections/ansible_collections/infrawatch
cp -r ./* %{buildroot}%{_datadir}/ansible/collections/ansible_collections/infrawatch

%files
%doc README*
%license LICENSE
%{_datadir}/ansible/collections/ansible_collections/infrawatch/
%{_datadir}/ansible/collections/ansible_collections/infrawatch/roles/osp_observability/

%changelog

