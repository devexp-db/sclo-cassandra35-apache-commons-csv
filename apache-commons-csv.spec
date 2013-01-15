%global base_name       csv
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.0
Release:          0.4.svn1071189%{?dist}
Summary:          Utilities to assist with handling of CSV files
License:          ASL 2.0
Group:            Development/Libraries
URL:              http://commons.apache.org/sandbox/%{base_name}
# svn export -r 1071189 http://svn.apache.org/repos/asf/commons/sandbox/csv/trunk/ apache-commons-csv-1.0
# tar caf apache-commons-csv-1.0.tar.xz apache-commons-csv-1.0
Source0:          %{name}-%{version}.tar.xz
BuildArch:        noarch

BuildRequires:    xmvn >= 0.2.1
BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    junit4
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    apache-commons-parent


%description
Commons CSV was started to unify a common and simple interface for
reading and writing CSV files under an ASL license.

%package javadoc
Summary:          API documentation for %{name}
Group:            Documentation
Requires:         jpackage-utils


%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
sed -i 's/\r//' *.txt
sed -i 's:commons-sandbox-parent:commons-parent:' pom.xml

%build
%mvn_file  : %{short_name} %{name}
%mvn_alias : %{short_name}:%{short_name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 15 2013 Michal Srb <msrb@redhat.com> - 1.0-0.4.svn1071189
- Build with xmvn
- Spec file cleanup

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.svn1071189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.svn1071189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.1.svn1071189
- Initial version of the package

