# revision 30524
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-common
Version:	20131009
Release:	6
Summary:	TeX Live documentation (common elements)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-common.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-common.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-common package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/index.html
%doc %{_texmfdistdir}/doc/texlive/texlive-common/examples/ex5.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-common/examples/ex6.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-common/examples/ex6a.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-common/examples/ex6b.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-common/examples/ex6c.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-common/install-lnx-main.png
%doc %{_texmfdistdir}/doc/texlive/texlive-common/psview.png
%doc %{_texmfdistdir}/doc/texlive/texlive-common/stdcoll.png
%doc %{_texmfdistdir}/doc/texlive/texlive-common/tlmgr-general-options.png
%doc %{_texmfdistdir}/doc/texlive/texlive-common/tlmgr-gui.png
%doc %{_texmfdistdir}/doc/texlive/texlive-common/tlmgr-paper-options.png
%doc %{_texmfdistdir}/doc/texlive/texlive-common/tray-menu.png
%doc %{_texmfdistdir}/doc/texlive/texlive-common/wizard-w32.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
