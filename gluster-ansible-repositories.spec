%global rolesdir %{_sysconfdir}/ansible/roles/gluster.repos
%global docdir %{_datadir}/doc/gluster.repos
%global buildnum 5

Name:      gluster-ansible-repositories
Version:   1.0.1
Release:   %{buildnum}%{?dist}
Summary:   Ansible roles for GlusterFS infrastructure management

URL:       https://github.com/gluster/gluster-ansible-repositories
Source0:   %{url}/archive/v%{version}-%{buildnum}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible-core >= 2.12

%description
Collection of Ansible roles for registering to Red Hat subscription manager,
subscribing to repositories, and installing packages.

%prep
%autosetup -p1 -n %{name}-%{version}-%{buildnum}

%build

%install
mkdir -p %{buildroot}/%{rolesdir}
cp -dpr defaults meta tasks LICENSE %{buildroot}/%{rolesdir}

mkdir -p %{buildroot}/%{docdir}
cp -dpr README.md examples %{buildroot}/%{docdir}

%files
%{rolesdir}
%doc %{docdir}

%license LICENSE

%changelog
* Fri Apr 01 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-5
- Rebase on v1.0.1-5

* Thu Feb 21 2019 Sachidananda Urs <sac@redhat.com> 1.0.0-1
- Bump the version number to 1

* Tue Oct 23 2018 Sachidananda Urs <sac@redhat.com> 0.2
- Address security concerns related to plaintext passwords

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release
