%{?scl:%scl_package apache-commons-csv}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}apache-commons-csv
Version:	1.4
Release:	3%{?dist}
Summary:	Utilities to assist with handling of CSV files
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-csv/
BuildArch:	noarch

Source0:	http://www.apache.org/dist/commons/csv/source/commons-csv-%{version}-src.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_java_common}apache-commons-io
BuildRequires:	%{?scl_prefix_java_common}junit
BuildRequires:	%{?scl_prefix_maven}apache-commons-lang3
BuildRequires:	%{?scl_prefix_maven}apache-commons-parent
BuildRequires:	%{?scl_prefix_maven}maven-antrun-plugin
%{?scl:Requires: %scl_runtime}

%description
Commons CSV was started to unify a common and simple interface for
reading and writing CSV files under an ASL license.

%package javadoc
Summary:	API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-csv-%{version}-src
sed -i 's/\r//' *.txt
find -name profile.jacoco -delete

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# Unwanted plugins
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin

# unwanted dependency
%pom_remove_dep :h2
rm src/test/java/org/apache/commons/csv/CSVPrinterTest.java

%mvn_file ":{*}" %{pkg_name} @1
%mvn_alias : commons-csv:
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Mon Mar 06 2017 Tomas Repik <trepik@redhat.com> - 1.4-3
- scl conversion

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 1.4-2
- Remove build dep on h2

* Thu Jun 23 2016 Michael Simacek <msimacek@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Mon Feb 15 2016 Michael Simacek <msimacek@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

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

