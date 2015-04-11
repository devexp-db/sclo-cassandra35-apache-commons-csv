%global base_name       csv
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.1
Release:          1%{?dist}
Summary:          Utilities to assist with handling of CSV files
License:          ASL 2.0
URL:              https://commons.apache.org/proper/%{short_name}/
Source0:          http://www.apache.org/dist/commons/csv/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(com.h2database:h2)
BuildRequires:    mvn(commons-io:commons-io)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:    mvn(org.jacoco:jacoco-maven-plugin)


%description
Commons CSV was started to unify a common and simple interface for
reading and writing CSV files under an ASL license.

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

# Unwanted plugins
%pom_remove_plugin :maven-assembly-plugin

# Prevent build failure
%pom_xpath_inject "pom:plugin[pom:artifactId='apache-rat-plugin']/pom:configuration/pom:excludes" "
<exclude>**/.xmvn/**</exclude>"

%mvn_file  : %{short_name} %{name}
%mvn_alias : %{short_name}:%{short_name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Sat Apr 11 2015 gil cattaneo <puntogil@libero.it> 1.1-1
- update to 1.1
- adapt to current guideline
- introduce license macro
- fix Url and Source0 field

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.svn1071189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.10.svn1071189
- Migrate BuildRequires from junit4 to junit

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.9.svn1071189
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.8.svn1071189
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.svn1071189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.svn1071189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.5.svn1071189
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Michal Srb <msrb@redhat.com> - 1.0-0.4.svn1071189
- Build with xmvn
- Spec file cleanup

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.svn1071189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.svn1071189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.1.svn1071189
- Initial version of the package

