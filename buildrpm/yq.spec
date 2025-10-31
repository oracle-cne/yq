
%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global package_name github.com/mikefarah/yq

%define name yq
%define version 4.47.2
%define release 1
%global golang_version 1.20.12
%global _buildhost build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:                   %{name}
Version:                %{version}
Release:                %{release}%{?dist}
Summary:                a lightweight and portable command-line YAML processor
License:                MIT
Url:                    https://github.com/mikefarah/yq
Source:                 %{name}-%{version}.tar.bz2
Vendor:                 Oracle America
BuildRequires:          golang >= %{golang_version}
BuildRequires:          jq

%description
A lightweight and portable command-line YAML processor. The aim of the project is to be the jq or sed of yaml files.

%prep
%setup -n %{name}-%{version}

%build
export GOPATH=$(go env GOPATH)
GOPATH_SRC=$GOPATH/src/%{package_name}
%__mkdir_p $GOPATH_SRC
%__rm -r $GOPATH_SRC
%__ln_s $PWD $GOPATH_SRC

pushd $GOPATH_SRC
git_short_ver=`curl -sS https://api.github.com/repos/mikefarah/yq/git/refs/tags/v%{version} | jq -r '.object.sha' | colrm 8`
LDFLAGS="-X main.GitCommit=${git_short_ver} -X main.GitDescribe=%{version}"
go build -v -o %{name} --ldflags "${LDFLAGS}"
popd

%install
%__install -D -m 0755 %{name}  %{buildroot}/usr/bin/%{name}

%files
%license LICENSE THIRD_PARTY_LICENSES.txt
%attr(755,root,root) /usr/bin/%{name}

%clean
rm -fr %{buildroot}
rm -fr %{_builddir}/%{name}-%{version}

%changelog
* Fri Oct 31 2025 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 4.47.2-1
- Added Oracle specific build files
