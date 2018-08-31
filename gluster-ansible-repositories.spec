%global rolesdir %{_sysconfdir}/ansible/roles/gluster.repos
%global docdir %{_datadir}/doc/gluster.repos

Name:      gluster-ansible-repositories
Version:   0.1
Release:   1%{?dist}
Summary:   Ansible roles for GlusterFS infrastructure management

URL:       https://github.com/gluster/gluster-ansible-repositories
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible >= 2.6

%description
Collection of Ansible roles for registering to Red Hat subscription manager,
subscribing to repositories, and installing packages.

%prep
%setup -q -n %{name}-%{version}

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
* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release
