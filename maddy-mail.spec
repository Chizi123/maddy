Name:          	maddy-mail
Version:        0.5.1
Release:        1%{?dist}
Summary:        Go based email server

License:        GPLv3
URL:            https://maddy.email/
Source0:        https://github.com/foxcpp/maddy/maddy-v%{version}.tar.gz

BuildRequires:  golang gcc make scdoc
#Requires:  	

%define debug_package %{nil}

%description
Maddy is an all in one email server written in go.

%prep
%setup -qn maddy-%{version}
#cd ..
#mv maddy-%{version} %{name}-%{version}

%build
# %make_build
./build.sh


%install
rm -rf $RPM_BUILD_ROOT
# %make_install
./build.sh --destdir "${RPM_BUILD_ROOT}" --prefix "/usr" install

%files
%license COPYING
#%doc add-docs-here
/usr/bin/maddy
/usr/bin/maddyctl
%config(noreplace) /etc/maddy/maddy.conf
/usr/lib/systemd/system/maddy.service
/usr/lib/systemd/system/maddy@.service
%doc /usr/share/man/man1/maddy.1.gz
%doc /usr/share/man/man5/maddy{,-auth,-blob,-config,-filters,-imap,-smtp,-storage,-tables,-targets,-tls}.5.gz


%changelog
* Thu Sep  25 2021 Created 
- 
