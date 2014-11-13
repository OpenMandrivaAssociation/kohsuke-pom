Name:           kohsuke-pom
Version:        9
Release:        1%{?dist}
Summary:        Kohsuke parent POM

# License is specified in pom file
License:        MIT
URL:            https://github.com/kohsuke/pom
Source0:        https://github.com/kohsuke/pom/archive/pom-%{version}.tar.gz
Source1:        https://raw.github.com/kohsuke/youdebug/youdebug-1.5/LICENSE.txt

BuildArch:      noarch

BuildRequires:  maven-local

%description
This package contains Kohsuke parent POM file.

%prep
%setup -q -n pom-pom-%{version}

cp %{SOURCE1} LICENSE

# we don't have these plugins and extensions
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-gitsite']]"
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :gmaven-plugin

# missing dep org.kohsuke:doxia-module-markdown
%pom_remove_plugin :maven-site-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Thu Jul 03 2014 Michal Srb <msrb@redhat.com> - 9-1
- Update to upstream version 9

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-2
- Rebuild to regenerate Maven auto-requires

* Mon Apr 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-1
- Update to upstream version 8

* Fri Feb 28 2014 Michal Srb <msrb@redhat.com> - 7-1
- Update to upstream version 7

* Thu Feb 20 2014 Michal Srb <msrb@redhat.com> - 6-2
- Fix FTBFS

* Fri Aug 09 2013 Michal Srb <msrb@redhat.com> - 6-1
- Update to upstream version 6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Michal Srb <msrb@redhat.com> - 5-1
- Initial package

