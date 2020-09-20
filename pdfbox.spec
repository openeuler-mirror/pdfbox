Name:          pdfbox
Version:       2.0.9
Release:       7
Summary:       A Java PDF Library
License:       ASL 2.0
URL:           http://pdfbox.apache.org/
Source0:       http://archive.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip
Patch6000:     CVE-2018-8036.patch
Patch6001:     CVE-2018-11797.patch
BuildRequires: maven-local mvn(commons-io:commons-io)
BuildRequires: mvn(commons-logging:commons-logging) mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17) mvn(org.apache.ant:ant) mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin) mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on) dejavu-sans-mono-fonts google-noto-emoji-fonts
BuildRequires: liberation-sans-fonts icc-profiles-openicc fontconfig
Requires:      liberation-sans-fonts

BuildArch:     noarch
Obsoletes:     pdfbox-ant < 2.0.16-%{release} jempbox < 2.0.16-%{release} pdfbox-examples < 2.0.16-%{release}

%description
Apache PDFBox is an open source Java PDF library for working with PDF
documents. This project allows creation of new PDF documents, manipulation of
existing documents and the ability to extract content from documents. Apache
PDFBox also includes several command line utilities. Apache PDFBox is
published under the Apache License v2.0.

%package debugger
Summary: Apache PDFBox Debugger

%description debugger
This package contains the PDF debugger for Apache PDFBox.

%package tools
Summary: Apache PDFBox Tools

%description tools
This package contains command line tools for Apache PDFBox.

%package javadoc
Summary: Javadoc for pdfbox

%description javadoc
This package contains the API documentation for pdfbox

%package -n fontbox
Summary: Apache FontBox

%description -n fontbox
FontBox is a Java library used to obtain low level information from font
files. FontBox is a subproject of Apache PDFBox.

%package parent
Summary: Apache PDFBox Parent POM

%description parent
Apache PDFBox Parent POM.

%package reactor
Summary: Apache PDFBox Reactor POM

%description reactor
Apache PDFBox Reactor POM.

%package -n preflight
Summary: Apache Preflight

%description -n preflight
The Apache Preflight library is an open source Java tool that implements 
a parser compliant with the ISO-19005 (PDF/A) specification.

%package -n xmpbox
Summary: Apache XmpBox

%description -n xmpbox
The Apache XmpBox library is an open source Java tool that implements Adobe's
XMP(TM) specification.  It can be used to parse, validate and create xmp
contents.  It is mainly used by subproject preflight of Apache PDFBox.

%prep
%autosetup -p1


%pom_disable_module preflight-app
%pom_disable_module debugger-app
%pom_disable_module app
%pom_disable_module examples

%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-download-plugin
%pom_remove_plugin -r :download-maven-plugin

%pom_remove_dep -r com.github.jai-imageio:
%pom_remove_dep -r :jbig2-imageio
%pom_remove_dep :diffutils pdfbox

for fpath in tools/src/test/java/org/apache/pdfbox/tools/imageio/TestImageIOUtils.java \
             pdfbox/src/test/java/org/apache/pdfbox/text/TestTextStripper.java \
             pdfbox/src/test/java/org/apache/pdfbox/pdmodel/graphics/image/CCITTFactoryTest.java
do
    rm -f ${fpath}
done
sed -i -e 's/TestTextStripper/BidiTest/' pdfbox/src/test/java/org/apache/pdfbox/text/BidiTest.java


%mvn_file :pdfbox pdfbox
%mvn_file :pdfbox pdfbox
%mvn_file :pdfbox-debugger pdfbox-debugger
%mvn_file :pdfbox-examples pdfbox-examples
%mvn_file :pdfbox-tools pdfbox-tools
%mvn_file :preflight preflight
%mvn_file :xmpbox xmpbox
%mvn_file :fontbox fontbox

%build
%mvn_build -s -- -DskipITs -Dlucene.version=4 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-pdfbox
%doc README.md RELEASE-NOTES.txt

%files debugger -f .mfiles-pdfbox-debugger

%files tools -f .mfiles-pdfbox-tools

%files -n fontbox -f .mfiles-fontbox
%doc fontbox/README.txt LICENSE.txt NOTICE.txt

%files parent -f .mfiles-pdfbox-parent
%license LICENSE.txt NOTICE.txt

%files reactor -f .mfiles-pdfbox-reactor
%license LICENSE.txt NOTICE.txt

%files -n preflight -f .mfiles-preflight
%doc preflight/README.txt

%files -n xmpbox -f .mfiles-xmpbox
%doc xmpbox/README.txt LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Sat Sep 19 2020 zhanghua <zhanghua40@huawei.com> - 2.0.9-7
- Fix CVE-2018-8036, CVE-2018-11797

* Fri Feb 28 2020 Senlin Xia <xiasenlin1@huawei.com> - 2.0.9-6
- package init
